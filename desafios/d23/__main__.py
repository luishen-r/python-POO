from poligono import *


def main():
    q = Quadrado(5)
    print(f'Um quadrado de  lado {q.lado}m tem perimetro igual a {q.perimetro()}m e área igual a {q.area()}m²')
    
    c = Circulo(3)
    print(f'Um circulo de raio {c.raio}m tem perimetro {c.perimetro()}m e área de {c.area()}m²')

if __name__ == "__main__":
    main()