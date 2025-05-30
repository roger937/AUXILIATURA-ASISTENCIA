#PEDIR 5 NUMEROS Y GUARDARLOS EN UNA LISTA E IMPRIMIR LA SUMA Y EL PROMEDIO
numeros = []
for i in range(5):
    num = float(input(f"Ingresa un numero: "))
    numeros.append(num)

suma = sum(numeros)
promedio = suma / len(numeros)

print(f"Suma de los numeros: {suma}")
print(f"Promedio de los numeros: {promedio}")