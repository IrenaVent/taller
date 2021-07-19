import sys # de system

argumentos = sys.argv 
# aquí van a estar las palabras despues de python
# nos va a dar una array (lista) con unas serie de argumentos posicionales,
# de tal manera que después de python de tal manera que:
# python cambiapalabra.py fichero.txt TIZAS LACRAS:
# elemento 0 será "cambiapalabra"
# elemento 1 será "fichero.txt"
# etc

nombreF = argumentos[1] 
original = argumentos [2]
nueva = argumentos [3]


f = open(nombreF,"r")  # abrir archivo modo lectura

texto_original = f.read() # metemos el texo en una variable con la que podemos trabajar
f.close() # cerramos

texto_sustituido = texto_original.replace(original, nueva)

f = open(nombreF,"w") # abrir archivo modo escritura

f.write(texto_sustituido) # sobreescribir el texto 
f.close()

