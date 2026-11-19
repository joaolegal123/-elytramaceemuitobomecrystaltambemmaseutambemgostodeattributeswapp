import math as m

def soma(a: float, b: float) -> float:
    return a + b

def subtracao(a: float, b: float) -> float:
    return a - b

def multiplicacao(a: float, b: float) -> float:
    return a * b

def divisao(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Não é possivel dividir por zero")
    return a /b

def potencia(a: float, b: float) -> float:
    return m.pow(a, b)

def raiz_quadrada(a: float, b: float) -> float:
    if a < 0:
        raise ValueError("Não é possivel calcular a raiz quadrada de um númo negativo.")
    return m.sqrt(a)