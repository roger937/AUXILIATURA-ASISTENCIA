class Animal:
    def __init__(self, nombrex, especiex, edadx):
        self.nombre = nombrex
        self.especie = especiex
        self.edad = edadx

    def describir(self):
        return f"{self.nombre} es un {self.especie} y tiene {self.edad} años."

mi_animal = Animal("max", "perro", 3)
 
print(mi_animal.describir())