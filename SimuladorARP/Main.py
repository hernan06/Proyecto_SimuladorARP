'''
Created on 03/01/2013
@author: Hernan
'''
import pygame

from Bus import Bus
from Palette import Palette
from Host import Host
from Router import Router
from Simulacion import Simulacion

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN,0)
    exit=True
    Palette1=Palette()
    c1 = pygame.time.Clock()
    while True and exit!=0:
        c1.tick(100)
        exit=Palette1.ARPDesign(screen)
        if(exit>0 and exit<5):
            Simulacion1=Simulacion()
            Simulacion1.ARPSimulation(screen,exit)
        else:
            if(exit==5):
                Simulacion1=Simulacion()
                Simulacion1.ARPSimulationCase5(screen)
main()
    
