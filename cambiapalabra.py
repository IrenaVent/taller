original = "tizas"
nueva = "yesos"

nombreF = "fichero.txt"

f = open(nombreF,"r")  # abrir archivo modo lectura

texto_original = f.read() # metemos el texo en una variable con la que podemos trabajar
f.close() # cerramos

texto_sustituido = texto_original.replace(original, nueva)

f = open(nombreF,"w") # abrir archivo modo escritura

f.write(texto_sustituido) # sobreescribir el texto 
f.close()

