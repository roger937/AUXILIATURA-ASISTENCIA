# Definicion de la clase base llamada Animal
class Animal:
    def __init__(self, nombre, edad):
        # Atributos: nombre y edad del animal
        self.nombre = nombre
        self.edad = edad

    def emitir_sonido(self):
        # Metodo generico que sera sobrescrito en las clases hijas
        print("Este animal hace un sonido")

# Definicion de la clase hija Perro
class Perro(Animal):
    def emitir_sonido(self):
        print("Guau Guau")

# Definicion de la clase hija Gato
class Gato(Animal):
    def emitir_sonido(self):
        print("Miau")

# Definicion de la clase hija Pajaro
class Pajaro(Animal):
    def emitir_sonido(self):
        print("Pío pío")

# Funcion que recibe una lista de animales y llama a emitir_sonido() de cada uno
def hacer_emitir_sonido(animales: list):
    for animal in animales:
        animal.emitir_sonido()

# Ejemplo de uso 
if __name__ == "__main__":
    animales = [
        Perro("Max", 4),
        Gato("Luna", 2),
        Pajaro("Pepe", 1)
    ]
    hacer_emitir_sonido(animales)
