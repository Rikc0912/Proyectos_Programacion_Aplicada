import math

class OperacionesBasicas:
    def __init__(self):
        self.val = 0
        self.val2 = 0
        self.r = 0

    def getVal(self):
        return self.val

    def setVal(self, valor):
        self.val = valor

    def getVal2(self):
        return self.val2

    def setVal2(self, valor):
        self.val2 = valor

    def getR(self):
        return self.r

    def setR(self, valor):
        self.r = valor

    # Operaciones básicas
    def sumar(self, a, b):
        self.r = a + b
        return self.r

    def restar(self, a, b):
        self.r = a - b
        return self.r

    def multiplicar(self, a, b):
        self.r = a * b
        return self.r

    def dividir(self, a, b):
        if b == 0:
            print("Error: No se puede dividir por cero.")
            return None
        else:
            self.r = a / b
            return self.r

    # Operaciones algebraicas
    def potencia(self, a, b):
        self.r = a ** b
        return self.r

    def raiz_cuadrada(self, a):
        if a < 0:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
            return None
        self.r = math.sqrt(a)
        return self.r

    def logaritmo(self, a):
        if a <= 0:
            print("Error: El logaritmo solo está definido para números positivos.")
            return None
        self.r = math.log10(a)
        return self.r

    def mostrarResultado(self):
        print(f"El resultado es: {self.r}")
