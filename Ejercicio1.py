
### Marlon Sebastian Conejo ###

####   ABECEDARIO   ####

# Ejercicio 1: Lista abecedario Escribir un programa que almacene el abecedario
# en una lista, elimine de la lista las letras que ocupen
# posiciones múltiplos de n, y muestre por pantalla
# la lista resultante

# Entrada: Una lista con el abecedario Un numero n

# Salida: Una lista de salida donde solamente se encuentren las
# letras que no ocupan posiciones multipolos de n

listaAbecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("La lista es:")
print()
print(listaAbecedario)
print()

nueva_lista = [letra for i, letra in enumerate (listaAbecedario, 1)
               if i % 2 !=0]

print("Eliminando los multiplos de n, la lista resultante es: ")
print()
print(nueva_lista)