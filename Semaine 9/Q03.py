from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nom):
        self.nom = nom
    
    @abstractmethod
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        return "Wouf"

class Chat(Animal):
    def parler(self):
        return "Miaou"
    
chien = Chien("Bob")
chat = Chat("Mimi")

print(chien.nom, "dit", chien.parler())
print(chat.nom, "dit", chat.parler())

