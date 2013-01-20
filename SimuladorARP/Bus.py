'''
Created on 03/01/2013

@author: Hernan
'''
import pygame

class Bus():
    Linea=None
    point_start=(0,0)
    point_end=(0,0)
    element_start=None
    element_end=None
    Black=(100,0,0)
    
    def __init__(self,x1,y1,x2,y2):
        self.point_start=(x1,y1)
        self.point_end=(x2,y2)
    
    def drawpoint(self,screen):
        pygame.draw.line(screen,self.Black,self.point_start,self.point_end,3)
    
    
   