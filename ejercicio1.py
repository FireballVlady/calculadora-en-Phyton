print("Calculadora en phyton")
print("selecciona una opcion")
print("1 = suma")
print("2 = multiplicacion")
print("3 = divicion")
print("4 = resta")
operador = int(input("ingresa una opcion "))
numero = int(input("ingresa el primer numero "))
numero2 = int(input("ingresa el segundo numero "))
resultado = 0
if operador == 1:
    resultado = numero + numero2
    print ("Resultado de la suma", resultado) 
elif operador == 2:
    resultado = numero * numero2
    print("Resulatdo de la multiplicacion ", resultado)
elif operador == 3:
    resultado = numero / numero2
    print("resultado de divicion ", resultado)
elif operador == 4:
    resultado = numero - numero2
    print("resultado de la resta ", resultado)
else:
    print("error dato no valido")