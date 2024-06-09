import math

def distancia_puntos(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "equilátero"
    elif a == b or b == c or a == c:
        return "isósceles"
    else:
        return "escaleno"

def es_triangulo(x1, y1, x2, y2, x3, y3):
    lado1 = distancia_puntos(x1, y1, x2, y2)
    lado2 = distancia_puntos(x2, y2, x3, y3)
    lado3 = distancia_puntos(x3, y3, x1, y1)
    return lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2

def area_triangulo(x1, y1, x2, y2, x3, y3):
    lado1 = distancia_puntos(x1, y1, x2, y2)
    lado2 = distancia_puntos(x2, y2, x3, y3)
    lado3 = distancia_puntos(x3, y3, x1, y1)
    s = (lado1 + lado2 + lado3) / 2
    area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))
    return area

def main():
    print("Ingrese las coordenadas (x, y) de los tres puntos que forman el triángulo:")
    x1, y1 = map(float, input("Punto 1 (x1 y1): ").split())
    x2, y2 = map(float, input("Punto 2 (x2 y2): ").split())
    x3, y3 = map(float, input("Punto 3 (x3 y3): ").split())

    if es_triangulo(x1, y1, x2, y2, x3, y3):
        lado1 = distancia_puntos(x1, y1, x2, y2)
        lado2 = distancia_puntos(x2, y2, x3, y3)
        lado3 = distancia_puntos(x3, y3, x1, y1)
        tipo = tipo_triangulo(lado1, lado2, lado3)
        area = area_triangulo(x1, y1, x2, y2, x3, y3)
        print(f"Los puntos ingresados forman un triángulo {tipo} con área {area:.2f}.")
    else:
        print("Los puntos ingresados no forman un triángulo.")

if __name__ == "__main__":
    main()
