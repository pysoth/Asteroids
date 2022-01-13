import random

from pygame.math import Vector2

import core


class Asteroids:
    def __init__(self):
        self.position=Vector2(random.randint(0,400),random.randint(0,400))
        self.vitesse = Vector2(0,0)
        self.acceleration = Vector2(0,0)
        self.vivante = True

        self.couleur = (255,255,0)
        self.taille = 5

        self.maxVitesse = 5
        self.maxAcceleration = 1

    def afficher(self):
        if self.vivante:
            core.Draw.circle(self.couleur,self.position,self.taille)
        else:
            core.Draw.circle((255,255,0),self.position,self.taille)


    def deplacement(self):






    def bordure(self,fenetre):
        if self.position.y<0:
            self.position.y < fenetre[1]

        if self.position.y > fenetre[1]:
            self.position.y > 0

        if self.position.x < 0:
            self.position.x < fenetre[0]

        if self.position.x > fenetre[0]:
            self.position.x > 0