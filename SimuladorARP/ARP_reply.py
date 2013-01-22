'''
Created on 16/01/2013

@author: Hernan
'''
import pygame

class ARP_reply():
    
    
    def __init__(self,x,y,HostS,HostD):
        self.Arp_message=None
        self.ipSource=None
        self.macSource=None
        self.ipDestination=None
        self.macDestination="ff-ff-ff-ff"
        self.Arp_message=self.createSprite(x,y,"Images/arp_response2.jpg")        
        self.ipSource=HostS.adressIP
        self.macSource=HostS.adressMac
        self.ipDestination=HostD.adressIP
        self.macDestination=HostD.adressMac
        self.display=pygame.display.get_surface()
    
    def createSprite(self,x,y,adr):
        s1 = pygame.sprite.Sprite()
        s1.image = pygame.image.load(adr).convert_alpha()
        s1.rect = s1.image.get_rect()
        (s1.rect.left, s1.rect.top) = (x,y)
        return s1
    
    def MoveARP(self,dir):
        if(dir==1):
            Vx=1
            Vy=0
        if(dir==2):
            Vx=-1
            Vy=0
        if(dir==3):
            Vx=0
            Vy=1
        if(dir==4):
            Vx=0
            Vy=-1
        self.Arp_message.rect.move_ip(Vx,Vy)
        
    def update(self,screen):
        screen.blit(self.Arp_message.image,self.Arp_message.rect)