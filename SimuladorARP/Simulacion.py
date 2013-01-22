'''
Created on 13/01/2013

@author: Hernan
'''
import pygame
import random
from Host import Host
from Router import Router
from Bus import Bus
from pygame.gp2x.constants import BUTTON_A
from ARP_request import ARP_request
from ARP_reply import ARP_reply 
from Ping import Ping

class Simulacion():
    
    def __init__(self):
        self.element1=None
        self.element2=None
        self.button_exit=None
        self.button_clear=None
        self.arp_request=None
        self.arp_repply=None
        self.Bus1=None
        self.panel=None
        self.ping=None
        self.panelList=[]
        self.exit1=pygame.image.load("button_back1.jpg")
        self.exit2=pygame.image.load("button_back2.jpg")
        self.clear1=pygame.image.load("button_clear1.jpg")
        self.clear2=pygame.image.load("button_clear2.jpg")
        self.display=pygame.display.get_surface()
    
    def randomMAC(self):
        mac = [ 0x00, 0x16, 0x3e,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]
        return ':'.join(map(lambda x: "%02x" % x, mac))
    
    def createSprite(self,x,y,adr):
        s1 = pygame.sprite.Sprite()
        s1.image = pygame.image.load(adr).convert_alpha()
        s1.rect = s1.image.get_rect()
        (s1.rect.left, s1.rect.top) = (x,y)
        return s1       
    
    def createCase1(self):
        self.element1=Host(100,200,"192.168.1.2",self.randomMAC())
        self.element2=Host(700,200,"192.168.1.3",self.randomMAC())
        
    def createCase2(self):
        self.element1=Host(100,200,"192.168.1.2",self.randomMAC())
        self.element2=Router(700,200,"192.168.1.1",self.randomMAC())
    
    def createCase3(self):
        self.element1=Router(100,200,"192.168.1.1",self.randomMAC())
        self.element2=Router(700,200,"192.158.1.1",self.randomMAC())
        
    
    def createCase4(self):
        self.element1=Router(100,200,"192.168.1.1",self.randomMAC())
        self.element2=Host(700,200,"192.168.1.2",self.randomMAC())
        
        
    def update(self,screen,move,flagSource):
        x,y=pygame.mouse.get_pos()
        self.Bus1.drawpoint(self.display)
        if(move==1):
            if(flagSource==1):
                self.arp_request.MoveARP(1)
            else:
                if(flagSource==2):
                    self.arp_request.MoveARP(2)
            self.arp_request.update(screen)
        else:
            if(move==2):
                if(flagSource==1):
                    self.arp_repply.MoveARP(2)
                else:
                    if(flagSource==2):
                        self.arp_repply.MoveARP(1)
                self.arp_repply.update(screen)
        if(self.button_exit.rect.collidepoint(x,y)):
            self.button_exit.image=self.exit2
        else:
            self.button_exit.image=self.exit1
        if(self.button_clear.rect.collidepoint(x,y)):
            self.button_clear.image=self.clear2
        else:
            self.button_clear.image=self.clear1
        self.element1.update(screen,0)
        self.element2.update(screen,0)
        self.display.blit(self.panel.image,self.panel.rect)
        self.display.blit(self.button_exit.image,self.button_exit.rect)
        self.display.blit(self.button_clear.image,self.button_clear.rect)
        self.printPanel(screen)
    
    def createSimulation(self,Case):
        if Case==1:
            self.createCase1()
        if Case==2:
            self.createCase2()
        if Case==3:
            self.createCase3()
        if Case==4:
            self.createCase4()
        if Case==5:
            self.createCase5()
        self.Bus1=Bus(100,205,700,205)
        self.button_exit=self.createSprite(1200, 5,"button_back1.jpg")
        self.button_clear=self.createSprite(1180, 670,"button_clear1.jpg")
        self.panel=self.createSprite(1000, 200,"panel.jpg")
        
    
    def printPanel(self,screen):
        for register in self.panelList:
            tmp=register
            if(tmp[2]==1):
                myfont = pygame.font.SysFont("LCD",16)
                label = myfont.render(tmp[0], 1,(220,0,0))
                screen.blit(label, (self.panel.rect.left,self.panel.rect.top+45))
                
                myfont = pygame.font.SysFont("LCD",16)
                label = myfont.render(tmp[1], 1,(220,0,0))
                screen.blit(label, (self.panel.rect.left+130,self.panel.rect.top+45))
            else:
                myfont = pygame.font.SysFont("LCD",16)
                label = myfont.render(tmp[0], 1,(220,0,0))
                screen.blit(label, (self.panel.rect.left,self.panel.rect.top+110))
                
                myfont = pygame.font.SysFont("LCD",16)
                label = myfont.render(tmp[1], 1,(220,0,0))
                screen.blit(label, (self.panel.rect.left+130,self.panel.rect.top+110))
            
    def ARPSimulation(self,screen,Case):
        self.createSimulation(Case)
        c1 = pygame.time.Clock()
        flag=True
        flag1=1
        flagC=True
        flagSource=0
        move=0
        SetDestination=False
        SetSource=False
        while True and flag:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if(self.button_exit.rect.collidepoint(x,y)):
                        flag=False
                    if(self.button_clear.rect.collidepoint(x,y)):
                        move=0
                        SetDestination=False
                        SetSource=False
                        flag1=1
                        flagC=True
                        self.panelList=[]
                        self.element1.Ips.pop(1)
                        self.element2.Ips.pop(1)
                    if events.button == 1: 
                        if self.element1.rect.collidepoint(x,y):
                            SetSource=True
                            x1,y1=self.element1.rect.right+2,self.element1.rect.top
                            flagSource=1
                            self.panelList.append([self.element1.adressIP,self.element1.adressMac,1])
                        if self.element2.rect.collidepoint(x,y):
                            SetSource=True
                            x1,y1=self.element2.rect.left,self.element2.rect.top
                            flagSource=2
                            self.panelList.append([self.element2.adressIP,self.element2.adressMac,1])
                    if events.button == 3: 
                        if self.element1.rect.collidepoint(x,y) and flagSource!=1:
                            SetDestination=True
                            x2,y2=self.element1.rect.left,self.element1.rect.top
                            self.panelList.append([self.element1.adressIP,self.element1.adressMac,2])
                        if self.element2.rect.collidepoint(x,y) and flagSource!=2:
                            SetDestination=True
                            x2,y2=self.element2.rect.left,self.element2.rect.top
                            self.panelList.append([self.element2.adressIP,self.element2.adressMac,2])
                    if(SetDestination and SetSource and flagC):
                        self.SendARP(x1,y1,x2,y2,flagSource)
                        self.SendARPRepply(x2, y2, x1, y1, flagSource)
                        flagC=False
                        
            c1.tick(100)
            screen.fill((255,255,255))
            if(SetDestination and SetSource):
                pygame.mouse.set_visible(False)
                pygame.mouse.set_pos([0,0])
                if(flagSource==1):
                    if(self.element2.rect.colliderect(self.arp_request.Arp_message.rect)):
                        if(self.arp_repply.Arp_message.rect.colliderect(self.element1.rect)):
                            move=3
                            self.ping=Ping(x1,y1)
                            dir=1
                            SetDestination=False
                            SetSource=False
                            flag1=1
                            flagC=True
                            self.element1.insert(self.element2.adressIP,self.element2.adressMac)
                            while move==3:
                                if self.ping.message.rect.colliderect(self.element2.rect):
                                    dir=2
                                if self.ping.message.rect.colliderect(self.element1.rect):
                                    move=0
                                screen.fill((255,255,255))                 
                                self.ping.MovePing(dir)
                                self.update(screen,move,flagSource)
                                self.ping.update(screen)
                                pygame.display.update()
                            self.panelList=[]
                            pygame.mouse.set_visible(True)
                        else:
                            if(flag1==1):
                                self.element2.insert(self.element1.adressIP,self.element1.adressMac)
                                move=2
                                flag1=0
                    else:
                        move=1
                       
                else:
                    if(self.element1.rect.colliderect(self.arp_request.Arp_message.rect)):
                        if(self.arp_repply.Arp_message.rect.colliderect(self.element2.rect)):
                            move=3
                            SetDestination=False
                            SetSource=False
                            flag1=1
                            flagC=True
                            pygame.mouse.set_visible(True)
                            self.ping=Ping(x1-131,y1)
                            dir=2
                            self.element2.insert(self.element1.adressIP,self.element1.adressMac)
                            while move==3:
                                if self.ping.message.rect.colliderect(self.element1.rect):
                                    dir=1
                                if self.ping.message.rect.colliderect(self.element2.rect):
                                    move=0
                                screen.fill((255,255,255))                 
                                self.ping.MovePing(dir)
                                self.update(screen,move,flagSource)
                                self.ping.update(screen)
                                pygame.display.update()
                            self.panelList=[]
                            
                        else:
                            if(flag1==1):
                                self.element1.insert(self.element2.adressIP,self.element2.adressMac)
                                move=2
                                flag1=0
                    else:
                        move=1
            self.update(screen,move,flagSource)
            pygame.display.update()
    
    
    
    
    def SendARP(self,x1,y1,x2,y2,flagSource):
        if flagSource==1:
            self.arp_request=ARP_request(x1,y1,self.element1,self.element2)
        else:
            self.arp_request=ARP_request(x1,y1,self.element2,self.element1)
        
    def SendARPRepply(self,x1,y1,x2,y2,flagSource):
        if flagSource==1:
            self.arp_repply=ARP_reply(x1,y1,self.element1,self.element2)
        else:
            self.arp_repply=ARP_reply(x1,y1,self.element2,self.element1)
        
        