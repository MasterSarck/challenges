# Reto #1
#  * ¿ES UN ANAGRAMA?
#  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso 
#    (Boolean) según sean o no anagramas.
#  * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra 
#    inicial.
#  * NO hace falta comprobar que ambas palabras existan.
#  * Dos palabras exactamente iguales no son anagrama.


def anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    if palabra1 == palabra2:
        return False
    else:
        palabra1 = str(sorted(palabra1))
        palabra2 = str(sorted(palabra2))
        if palabra1 == palabra2:
            return True
        else:
            return False

print(anagrama("Arma", "Arma"))