#escribe un programa que pida al usuario una lista de números 
#eparados por comas y luego calcule e imprima:
#la suma de todos los números
#el número más grande y el más pequeño
#cuántos números son pares y cuántos son impares
#Requisitos:
#Usar split() para convertir la entrada en una lista.
#Usar bucles y condicionales para recorrer y analizar los números.

en = input("ingresa una lista de numeros separados por comas: ")
num = [int(n) for n in en.split(',')]

sum_to = sum(num)
max = max(num)
min = min(num)

par = sum(1 for n in num if n % 2 == 0)
imp = len(num) - par

print("suma de todos los numeros:", sum_to)
print("numero mas grande:", max)
print("numero mas pequeno:", min)
print("cantidad de numeros pares:", par)
print("cantidad de numeros impares:", imp)