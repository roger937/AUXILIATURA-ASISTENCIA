#crea una función transponer_matriz(M) que retorne la transpuesta de una matriz M.
#ejemplo
#entrada: [[1, 2, 3], [4, 5, 6]]
#salida: [[1, 4], [2, 5], [3, 6]]
def pedir():
    fi = int(input("cuantas filas tiene la matriz ="))
    col = int(input("cuantas columnas tiene la matriz ="))
    ma = []

    print("ingresa los valores de la matriz fila por fila:")
    for i in range(fi):
        fi= input(f"Fila {i + 1}: ")
        num= list(map(int, fi.strip().split()))
        while len(num) != col:
            print(f"la fila debe tener exactamente {col} numero")
            fi = input(f"fila {i + 1} nuevamente: ")
            num= list(map(int, fi.strip().split()))
        ma.append(num)

    return ma

def transponer(M):
    fi = len(M)
    col = len(M[0])
    trans = []

    for j in range(col):
        nuevaf= []
        for i in range(fi):
            nuevaf.append(M[i][j])
        trans.append(nuevaf)

    return trans

ma= pedir()
trans = transponer(ma)

print("\nmatriz transpuesta:")
for fi in trans:
    print(fi)