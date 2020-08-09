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
#Codigo extraido de: https://sqreen.github.io/DevelopersSecurityBestPractices/timing-attack/python

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
#Funcion comun donde el atacante si encuentra el token extraido de: https://sqreen.github.io/DevelopersSecurityBestPractices/timing-attack/python
def str_equals(first_str, second_str):
    if len(first_str) != len(second_str):
        return False

    for c1, c2, in zip(first_str, second_str):
        if c1 != c2:
            return False
        time.sleep(0.01)
    return True

def str_equal2(first_str, second_str): #Funcion de defensa con un xor,  extraido de: https://paragonie.com/blog/2015/11/preventing-timing-attacks-on-string-comparison-with-double-hmac-strategy
    if len(first_str) != len(second_str):
        return False

    result = 0
    for x,y in zip (first_str, second_str):
        x =ord(x)
        y = ord(y)
        result |= x ^ y #Hacemos el XOR entre ambos str
        time.sleep(0.01) #Un timing para que todo tome el mismo tiempo
    return result == 0


#Funcion de defensa 2 usando un HMAC, extraido de: https://paragonie.com/blog/2015/11/preventing-timing-attacks-on-string-comparison-with-double-hmac-strategy
def str_equal3(first_str, second_str):
    arr = bytes(first_str, 'utf-8') #Se convierten los valores de str a bytes
    arr2 = bytes(second_str, 'utf-8')
    return( #Comparacion entre ambos str
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
    if str_equals(token, SECRET_TOKEN): #Linea para modificar 
        return 'Welcome,password correct'
    else:
        return 'Try better the next one', 403


if __name__=='__main__':
    app.run()
