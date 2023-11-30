# Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) 
# que sea capaz de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

def poligono (altura, base, lado, tipo):
    tipo = tipo.lower()
    if altura < 0 or base < 0 or lado < 0:
        return "Solo se admiten números positivos."
    
    if  tipo == "triangulo":
        #Triangulo
        area = (altura * base) * 0.5  
        return (f"base x altura (triangulo) = {area}")
    elif tipo == "cuadrado":
        #Cuadrado
        area = (lado * lado)
        return f"lado X lado (cuadrado) = {area}"
    
    elif tipo == "rectangulo":
        #Rectangulo
        area = (base * altura)
        return f"base X altura (rectangulo) = {area}"
    
print(poligono(2, 3, 4, "rectangulo"))