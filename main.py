import pygame

import core
from asteroids.Joueur import Joueur
from asteroids.asteroids import Asteroids


def setup():
    print('SetUp :')
    core.WINDOW_SIZE=[400,400]
    core.fps=30

    core.memory("proies",[])


    core.memory("nbPierres",100)


    for i in range(0,core.memory("nbPierres")):
        core.memory("Pierres").append(Pierres())





def run():


core.main(setup,run)