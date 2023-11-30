#  * ¿ES UN NÚMERO PRIMO?
#  * Dificultad: MEDIA
#  * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.




for num in range(1, 101):
    es_divisible = False

    for dividir in range(2, num):
        if num % dividir == 0:
            es_divisible = True 
            print(f"{num} no es primo")
            break

    if not es_divisible:
        print(f"{num} es primo")


# numero = 14                                       10 / 2...10
# es_divisible = False                              if numero % 2 == 0: Se puede dividir
# for divisor in range(2, numero):                  if numero % 2 != 0: No se puede dividir
#     if numero % divisor == 0:
#         es_divisible = True
#         break
#     if not es_divisible:
#        print(f"Felicidades! {numero} es primo")