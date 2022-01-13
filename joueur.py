import random

from pygame.math import Vector2

import core


class Joueur:
    def __init__(self):
        self.position = Vector2(random.randint(0, 400), random.randint(0, 400))
        self.vitesse = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)

        self.couleur = (255, 0, 255)
        self.taille = 10

        self.maxVitesse = 6
        self.maxAcceleration = 4



    def afficher(self):
        core.Draw.circle(self.couleur, self.position, self.taille)

    def deplacement(self,Asteroids):





    def bordure(self,fenetre):
        if self.position.y < 0:
            self.position.y < fenetre[1]

        if self.position.y > fenetre[1]:
            self.position.y > 0

        if self.position.x < 0:
            self.position.x < fenetre[0]

        if self.position.x > fenetre[0]:
            self.position.x > 0

    def tirer(self,pierres):
        for p in pierres:
            if p.position.distance_to(self.position)<self.taille+p.taille:
                p.vivante = False