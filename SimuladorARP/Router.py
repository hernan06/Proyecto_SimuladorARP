'''
Created on 03/01/2013

@author: Hernan
'''
import pygame
import random

class Router(pygame.sprite.Sprite):
   
    
    def __init__(self,x,y,ip,mac):
        pygame.sprite.Sprite.__init__(self)
        self.adressIP=None
        self.adressMac=None
        self.arp_table=None
        self.Ips=[]
        self.ListHost=[]
        self.registro=None
        
        self.image = pygame.image.load("ROUTER.jpg")
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top=x,y
        self.arp_table=self.createSprite(self.rect.left,self.rect.bottom, "arp_table.jpg")
        
        self.adressIP=ip
        self.adressMac=mac
        self.Ips.append([self.adressIP,self.adressMac])
    
    def createSprite(self,x,y,adr):
        s1 = pygame.sprite.Sprite()
        s1.image = pygame.image.load(adr).convert_alpha()
        s1.rect = s1.image.get_rect()
        (s1.rect.left, s1.rect.top) = (x,y)
        return s1 
    
    def insert(self,ip,mac):
        date=[ip,mac]
        for register in self.Ips:
            if register==date:
                return
        self.Ips.append([ip,mac]) 
        
    def update(self,screen,f):
        screen.blit(self.image,self.rect)
        screen.blit(self.arp_table.image,self.arp_table.rect)
        self.UpdateTable(screen,f)
    
    def UpdateTable(self,screen,f):
        x=self.arp_table.rect.left
        y=self.arp_table.rect.bottom
        for register in self.Ips:
            self.registro=self.createSprite(x, y,"registro.jpg")
            screen.blit(self.registro.image,self.registro.rect)
            if(f==0):
                tmp=register
                myfont = pygame.font.SysFont("LCD",12)
                label = myfont.render(tmp[0], 1,(220,0,0))
                screen.blit(label, (self.registro.rect.left,y+3))
                myfont = pygame.font.SysFont("LCD",12)
                label = myfont.render(tmp[1], 1,(220,0,0))
                screen.blit(label, (self.registro.rect.left+85,y+3))
            y=y+22

