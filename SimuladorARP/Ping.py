'''
Created on 21/01/2013

@author: Hernan
'''
import pygame

class Ping():
    def __init__(self,x,y):
        self.message=None
        self.message=self.createSprite(x,y,"Images/Ping.jpg")
        
    def createSprite(self,x,y,adr):
        s1 = pygame.sprite.Sprite()
        s1.image = pygame.image.load(adr).convert_alpha()
        s1.rect = s1.image.get_rect()
        (s1.rect.left, s1.rect.top) = (x,y)
        return s1
    
    def MovePing(self,dir):
        if(dir==1):
            Vx=1
            Vy=0
        if(dir==2):
            Vx=-1
            Vy=0
        if(dir==3):
            Vx=0
            Vy=-1
        if(dir==4):
            Vx=0
            Vy=1
        self.message.rect.move_ip(Vx,Vy)
    
    def update(self,screen):
        screen.blit(self.message.image,self.message.rect)