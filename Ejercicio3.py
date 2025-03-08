#Ejercicio 3:
# transforme la cadena 
# ```El mejor regalo? El perdón...``` en ```el mejor perdón```
#  utilizando únicamente los métodos de listas que hemos visto.
#  La nueva cadena debe guardarse en la variable ```nueva_frase```:

frase = "El mejor regalo? el perdón..."
#la cadena en una lista de caracteres
list_frase = list(frase)  

# Eliminar caracteres no deseados
for char in "?.":
    while char in list_frase:
        list_frase.remove(char)

# dividimos las palabras
palabras = ''.join(list_frase).split()

# Eliminamos "regalo" y el segundo "El"
palabras.remove("regalo")
palabras.remove("el")

nueva_frase = ' '.join(palabras).lower()

print(nueva_frase)
