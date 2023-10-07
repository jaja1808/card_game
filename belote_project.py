import numpy as np
import random as rd


# definition de la classe carte
class carte:
    def __init__(self,nom_carte,couleur):
        self.__nom_carte=nom_carte
        self.__couleur=couleur

# 
    def get__nom_carte(self):
        return self.__nom_carte
    
    def get__couleur(self):
        return self.__couleur
   
    def set__nom_carte(self,nom_carte):
        self.__nom_carte=nom_carte
    
    def set__couleur(self,couleur):
        self.__couleur=couleur


# définition de la classe carte  attouf
class carte_atout(carte):
    def __init__(self, nom_carte, couleur,score):
        super().__init__(nom_carte, couleur)
        self.__score=score

    def get__score(self):
        return self.__score
    
    def set__score(self,score):
        self.__score=score


# définition de la classe  non attouf(normal)
class carte_normal(carte):
    def __init__(self, nom_carte, couleur,score):
        super().__init__(nom_carte, couleur)
        self.__score=score

    def get__score(self):
        return self.__score
    
    def set__score(self,score):
        self.__score=score


