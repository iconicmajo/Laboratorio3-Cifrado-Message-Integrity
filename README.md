# Laboratorio3-Cifrado-Message-Integrity
Laboratorio 3 de Cifrado de Información

### Requisitos
Instalar la siguiente libreria, para poder utilizar el método de AES

```pip install pycryptodome```

### Ejecución
Para parte 2.1 ejecutar ``` python laboratorio3-1.py```

Para parte 2.2 ejecutar ``` python server.py```

### Para ejecutar el Timing Attack:
En el archivo ``` python server.py``` modificar la linea 83 colocando ``` str_equals```
Ejecutar el archivo ``` python server.py```
Ejecutar en otro CMD el archivo  ``` python hack.py```

### Para ejecutar el Timing Attack con Defensa 1 (XOR):
En el archivo ``` python server.py``` modificar la linea 83 colocando ``` str_equal2```
Ejecutar el archivo ``` python server.py```
Ejecutar en otro CMD el archivo  ``` python hack.py```

### Para ejecutar el Timing Attack con Defensa 2 (HMAC):
En el archivo ``` python server.py``` modificar la linea 83 colocando ``` str_equal3```
Ejecutar el archivo ``` python server.py```
Ejecutar en otro CMD el archivo  ``` python hack.py```

### Demo Parte 2.1
[Video](https://youtu.be/YdSS5iGNTsA)

### Demo Parte 2.2
[Video](https://youtu.be/Jdx2bAPVVG8)
