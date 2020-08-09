"""
Laboratorio 3
Cifrado de información
#Maria Jose Castro 181202
#Diana de Leon 18607
#Camila Gonzalez 18398
#Maria Ines Vasquez 18250
#Christopher Barrios 18207
#Jose Garavito 18071
"""

#Ejercicio 2.2
#Codigo extraido de: https://pycryptodome.readthedocs.io/en/latest/src/hash/hmac.html

import time
from flask import Flask, request
import hmac
import hashlib
import math
import os

from Crypto.Cipher import *




app= Flask(__name__)

key= b'CC3078'

SECRET_TOKEN='ola'
#Funcion comun donde el atacante si encuentra el token
def str_equals(first_str, second_str):
    if len(first_str) != len(second_str):
        return False

    for c1, c2, in zip(first_str, second_str):
        if c1 != c2:
            return False
        time.sleep(0.01)
    return True

def str_equal2(first_str, second_str):
    if len(first_str) != len(second_str):
        return False

    result = 0
    for x,y in zip (first_str, second_str):
        x =ord(x)
        y = ord(y)
        result |= x ^ y
        time.sleep(0.01)
    return result == 0


#aqui voy a hacer la seguna defensa
def str_equal3(first_str, second_str):
    arr = bytes(first_str, 'utf-8')
    arr2 = bytes(second_str, 'utf-8')
    return(
    hmac.new( arr, b'Ggg','sha256').hexdigest()
    ==
    hmac.new(arr2, b'Ggg','sha256').hexdigest())

    #first_str = first_str.encode()
    #mac = hmac.new(key, first_str, hashlib.sha256)
    #if hmac.digest(key,mac, hashlib.sha256) == hmac.digest(key,second_str, hashlib.sha256):

def strcmp(s1, s2):
    if len(s1) !=len(s2):
        return False
    for c1,c2 in zip(s1,s2):
        return False
    time.sleep(0.01)
    return True

@app.route('/')
def protected():
    token= request.headers.get('X-TOKEN')

    if not token:
        return 'Missing token',401
    if str_equal3(token, SECRET_TOKEN):
        return 'Welcome,password correct'
    else:
        return 'Try better the next one', 403


if __name__=='__main__':
    app.run()
