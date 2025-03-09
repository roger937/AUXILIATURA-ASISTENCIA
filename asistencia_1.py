# ejercicio 1 : dar dos numeros y obtener la (+,-,*,/)

a = int(input("Ingresa un numero:  "))
b = int(input("Ingresa un numero:  "))


suma = a + b
resta = a - b
multiplicacion = a * b

if b != 0:
    division = a / b
else:
    division = "No se puede dividir por cero"

print(f"la suma es : {suma}")
print(f"la resta es : {resta}")
print(f"la multiplicacion es : {multiplicacion}")
print(f"la division es : {division}")




# ejercicio 2: saber si un numero es par o impar

num= int(input("Introduce un número: "))

if num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")
