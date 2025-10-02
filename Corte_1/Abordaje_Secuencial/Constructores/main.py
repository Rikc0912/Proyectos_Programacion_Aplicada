from OperacionesAlgebraicas import OperacionesBasicas

obj = OperacionesBasicas()

obj.setVal(20)
obj.setVal2(11)

# Suma
obj.sumar(obj.getVal(), obj.getVal2())
print("Suma:", obj.getR())

# Resta
obj.restar(obj.getVal(), obj.getVal2())
print("Resta:", obj.getR())

# Multiplicación
obj.multiplicar(obj.getVal(), obj.getVal2())
print("Multiplicación:", obj.getR())

# División
obj.dividir(obj.getVal(), obj.getVal2())
print("División:", obj.getR())

# Potencia (20^11)
obj.potencia(obj.getVal(), obj.getVal2())
print("Potencia:", obj.getR())

# Raíz cuadrada de 20
obj.raiz_cuadrada(obj.getVal())
print("Raíz cuadrada:", obj.getR())

# Logaritmo base 10 de 20
obj.logaritmo(obj.getVal())
print("Logaritmo base 10:", obj.getR())
