#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y 
# posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

lista = [random.randint(1, 10) for _ in range(10)]

resultado = [(num, num**2, num**3) for num in lista]

print(resultado)
