import sys # de system, para hablar con el intérprete, que en este caso es python


argumentos = sys.argv 
# aquí van a estar las palabras despues de python
# nos va a dar una array (lista) con unas serie de argumentos posicionales,
# de tal manera que después de python de tal manera que:
# python cambiapalabra.py fichero.txt TIZAS LACRAS:
# elemento 0 será "cambiapalabra"
# elemento 1 será "fichero.txt"
# etc
# lo que hacer .argv es guarda la lista y la intepreta, es decir si queremos
# interactuar con el propio intérprete, por ejemplo que la lista esta en el intérprete

if len (argumentos) < 2:
    f = input ("Nombre de fichero: ")
    argumentos.append(f)

if len (argumentos) < 3:
    argumentos.append(input("palabra original: "))

if len (argumentos) < 4:
    argumentos.append(input("nueva palabra: "))

# el orden es importante...porque va contando por la introducción de palabras

nombreFichero = argumentos[1] 
original = argumentos [2]
nueva = argumentos [3]
 
# ejercicio: hacer los inputs y si falta alguno de los elementos del fichos

f = open(nombreFichero,"r")  # abrir archivo modo lectura

texto_original = f.read() # metemos el texo en una variable con la que podemos trabajar
f.close() # cerramos

texto_sustituido = texto_original.replace(original, nueva)

f = open(nombreFichero,"w") # abrir archivo modo escritura

f.write(texto_sustituido) # sobreescribir el texto 
f.close()

