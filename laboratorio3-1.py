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

#Ejercicio 2.1
#Codigo extraido de: https://pycryptodome.readthedocs.io/en/latest/src/hash/hmac.html

from Crypto.Hash import HMAC, SHA256

print("Mensaje: Cifrado de informacion seccion 10")
print("Key: CC3078")
print("Respuesta de calculadora: 806c6e18554e70a4ab8ac88c9f644566faee92e0af00baf63e5e2933fa6ca9cd")

secret = b'CC3078'
msg=b'Cifrado de informacion seccion 10'
h = HMAC.new(secret, digestmod=SHA256)
h.update(msg)
print ("Nuestra respuesta: "+h.hexdigest())

print("--------------------------------------------------------------------------------------------------------------------")
print("Mensaje: La implementacion de este ejercicio fue sencilla")
print("Key: MAC")

print("Respuesta de calculadora: 665737ebf33ecf5e48b6c14fbaca2612c0bf9bf93d240bfd2dab9fe669900541")
secret = b'MAC'
msg=b'La implementacion de este ejercicio fue sencilla'
h = HMAC.new(secret, digestmod=SHA256)
h.update(msg)
print ("Nuestra respuesta: "+h.hexdigest())


