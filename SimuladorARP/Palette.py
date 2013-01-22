'''
Created on 10/01/2013

@author: Hernan
'''
import pygame
from Host import Host
from Router import Router
from Bus import Bus
pygame.init()

class Palette():
    
    
    def __init__(self):
        self.case1=None
        self.case2=None
        self.case3=None
        self.case4=None
        self.case5=None
        self.element1=None
        self.element2=None
        self.element3=None
        self.element4=None
        self.button_exit=None
        self.button_next=None
        self.Bus1=None
        self.Bus2=None
        self.case11=pygame.image.load("Images/Case1.1.jpg")
        self.case12=pygame.image.load("Images/Case1.2.jpg")
        self.case21=pygame.image.load("Images/Case2.1.jpg")
        self.case22=pygame.image.load("Images/Case2.2.jpg")
        self.case31=pygame.image.load("Images/Case3.1.jpg")
        self.case32=pygame.image.load("Images/Case3.2.jpg")
        self.case41=pygame.image.load("Images/Case4.1.jpg")
        self.case42=pygame.image.load("Images/Case4.2.jpg")
        self.case51=pygame.image.load("Images/Case5.1.jpg")
        self.case52=pygame.image.load("Images/Case5.2.jpg")
        self.exit1=pygame.image.load("Images/button_exit1.jpg")
        self.exit2=pygame.image.load("Images/button_exit2.jpg")
        self.next1=pygame.image.load("Images/button_next1.jpg")
        self.next2=pygame.image.load("Images/button_next2.jpg")
        self.createPalette()
        self.display=pygame.display.get_surface()
    
    def updatePalette(self):
        x,y=pygame.mouse.get_pos()
        if(self.case1.rect.collidepoint(x,y)):
            self.case1.image=self.case12
        else:
            self.case1.image=self.case11
            
        if(self.case2.rect.collidepoint(x,y)):
            self.case2.image=self.case22
        else:
            self.case2.image=self.case21
            
        if(self.case3.rect.collidepoint(x,y)):
            self.case3.image=self.case32
        else:
            self.case3.image=self.case31  
        if(self.case4.rect.collidepoint(x,y)):
            self.case4.image=self.case42
        else:
            self.case4.image=self.case41  
        if(self.case5.rect.collidepoint(x,y)):
            self.case5.image=self.case52
        else:
            self.case5.image=self.case51 
        if(self.button_exit.rect.collidepoint(x,y)):
            self.button_exit.image=self.exit2
        else:
            self.button_exit.image=self.exit1
        if(self.button_next.rect.collidepoint(x,y)):
            self.button_next.image=self.next2
        else:
            self.button_next.image=self.next1      
        
        self.display.blit(self.case1.image,self.case1.rect)
        self.display.blit(self.case2.image,self.case2.rect)
        self.display.blit(self.case3.image,self.case3.rect)
        self.display.blit(self.case4.image,self.case4.rect)
        self.display.blit(self.case5.image,self.case5.rect)
        self.display.blit(self.button_exit.image,self.button_exit.rect)
        self.display.blit(self.button_next.image,self.button_next.rect)
        
        rect=pygame.Rect(160, 0, 10,1000)
        pygame.draw.rect(self.display,(220,0,0),rect,0)
        
        myfont = pygame.font.SysFont("LCD", 75)
        label = myfont.render("ARP SIMULATOR", 1,(220,0,0))
        self.display.blit(label, (500, 15))
        
    def createCase1(self):
        self.element1=Host(300,200,0,0)
        self.element2=Host(900,200,0,0)
        self.Bus1=Bus(300,205,900,205)
        #self.arp_request.rect.left,self.arp_request.rect.top=300,200
        
    def createCase2(self):
        self.element1=Host(300,200,0,0)
        self.element2=Router(900,200,0,0)
        self.Bus1=Bus(300,205,900,205)
        
    def createCase3(self):
        self.element1=Router(300,200,0,0)
        self.element2=Router(900,200,0,0)
        self.Bus1=Bus(300,205,900,205)
    
    def createCase4(self):
        self.element1=Router(300,200,0,0)
        self.element2=Host(900,200,0,0)
        self.Bus1=Bus(300,205,900,205)
        
    def createCase5(self):
        self.element1=Host(300,200,0,0)
        self.element2=Host(1000,200,0,0)
        self.element3=Router(650,200,0,0)
        self.element4=Host(650,400,0,0)
        self.Bus1=Bus(300,205,1000,205)
        self.Bus2=Bus(660,200,660,400)
           
    def update(self,screen):  
        self.Bus1.drawpoint(screen)
        self.element1.update(screen,1)
        self.element2.update(screen,1)
    
    def update5(self,screen):
        self.Bus1.drawpoint(screen)
        self.Bus2.drawpoint(screen)
        self.element1.update(screen,1)
        self.element2.update(screen,1)
        self.element3.update(screen,1)
        self.element4.update(screen,1)
        
    def createSprite(self,x,y,adr):
        s1 = pygame.sprite.Sprite()
        s1.image = pygame.image.load(adr).convert_alpha()
        s1.rect = s1.image.get_rect()
        (s1.rect.left, s1.rect.top) = (x,y)
        return s1   
    
    def createPalette(self):
        self.case1=self.createSprite(10,40,"Images/Case1.1.jpg")
        self.case2=self.createSprite(self.case1.rect.left,self.case1.rect.bottom+20,"Images/Case2.1.jpg")
        self.case3=self.createSprite(self.case2.rect.left,self.case2.rect.bottom+20,"Images/Case3.1.jpg")
        self.case4=self.createSprite(self.case3.rect.left,self.case3.rect.bottom+20,"Images/Case4.1.jpg")
        self.case5=self.createSprite(self.case4.rect.left,self.case4.rect.bottom+20,"Images/Case5.1.jpg")
        self.button_exit=self.createSprite(1200, 5,"Images/button_exit1.jpg")
        self.button_next=self.createSprite(1200, 670,"Images/button_next1.jpg")
        
    def ARPDesign(self,screen):
        c1 = pygame.time.Clock()
        Case1Pressed=False
        Case2Pressed=False
        Case3Pressed=False
        Case4Pressed=False
        Case5Pressed=False
        flag=True
        while True and flag:
            for events in pygame.event.get():
                    if events.type == pygame.QUIT:
                        quit()
                    if events.type == pygame.MOUSEBUTTONDOWN:
                        x,y=pygame.mouse.get_pos()
                        if(self.case1.rect.collidepoint(x,y) and not(Case1Pressed)):
                            Case1Pressed=True
                            Case2Pressed=False
                            Case3Pressed=False
                            Case4Pressed=False
                            Case5Pressed=False
                            self.createCase1()
                        if(self.case2.rect.collidepoint(x,y)):
                            Case1Pressed=False
                            Case2Pressed=True
                            Case3Pressed=False
                            Case4Pressed=False
                            Case5Pressed=False
                            self.createCase2()
                        if(self.case3.rect.collidepoint(x,y)):
                            Case1Pressed=False
                            Case2Pressed=False
                            Case3Pressed=True
                            Case4Pressed=False
                            Case5Pressed=False
                            self.createCase3()
                        if(self.case4.rect.collidepoint(x,y)):
                            Case1Pressed=False
                            Case2Pressed=False
                            Case3Pressed=False
                            Case4Pressed=True
                            Case5Pressed=False
                            self.createCase4()
                        if(self.case5.rect.collidepoint(x,y)):
                            Case1Pressed=False
                            Case2Pressed=False
                            Case3Pressed=False
                            Case4Pressed=False
                            Case5Pressed=True
                            self.createCase5()
                        if(self.button_next.rect.collidepoint(x,y)):
                            flag=False
                        if(self.button_exit.rect.collidepoint(x,y)):
                            flag=False
                            return 0
                        
                              
            c1.tick(100)
            screen.fill((255,255,255))
            self.updatePalette()
            if(Case1Pressed or Case2Pressed or Case3Pressed or Case4Pressed):
                self.update(screen)
            if(Case5Pressed):
                self.update5(screen)
            pygame.display.update()
        if(Case1Pressed):
            return 1
        if(Case2Pressed):
            return 2
        if(Case3Pressed):
            return 3
        if(Case4Pressed):
            return 4
        if(Case5Pressed):
            return 5
    
           
