import random

from pygame.math import Vector2

import core

class Balles:
    def __init__(self):
        self.position=Vector2(random.randint(0,400),random.randint(0,400))
        self.vitesse = Vector2(0,0)


        self.couleur = (0,255,0)
        self.taille = 5

        self.maxVitesse = 5

    def afficher(self):

            core.Draw.circle((0,255,0),self.position,self.taille)



    def bordure(self,fenetre):
        if self.position.y<0:
            self.position.y < fenetre[1]

        if self.position.y > fenetre[1]:
            self.position.y > 0

        if self.position.x < 0:
            self.position.x < fenetre[0]

        if self.position.x > fenetre[0]:
            self.position.x > 0