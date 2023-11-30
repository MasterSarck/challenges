#  * Reto #2
#  * LA SUCESIÓN DE FIBONACCI
#  * Dificultad: DIFÍCIL
#  *
#  * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de 
#    Fibonacci empezando en 0.
#  * La serie Fibonacci se compone por una sucesión de números en la que el sig siempre
#    es la suma de los dos anteriores.
#  * 0, 1, 1, 2, 3, 5, 8, 13...

num1 = 0
num2 = 1
sig = 0
for i in range(0, 51): 
    sig = num1 + num2
    num1 = num2
    num2 = sig
    print(sig)