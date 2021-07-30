class Animal:
    def getData(self):
        return "Animal"

class Gato(Animal):
    def getData(self):
        return "Gato"

g = Gato()
print(g.getData())
