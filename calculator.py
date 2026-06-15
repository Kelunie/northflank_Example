class Calculator:
    #Clase simple para operaciones básicas de la calculadora.

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    def power(self, a: float, b: float) -> float:
        return a ** b
