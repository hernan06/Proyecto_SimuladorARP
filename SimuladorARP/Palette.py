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
    case1=None
    case2=None
    case3=None
    case4=None
    case5=None
    element1=None
    element2=None
    button_exit=None
    button_next=None
    Bus1=None
    case11=pygame.image.load("Case1.1.jpg")
    case12=pygame.image.load("Case1.2.jpg")
    case21=pygame.image.load("Case2.1.jpg")
    case22=pygame.image.load("Case2.2.jpg")
    case31=pygame.image.load("Case3.1.jpg")
    case32=pygame.image.load("Case3.2.jpg")
    case41=pygame.image.load("Case4.1.jpg")
    case42=pygame.image.load("Case4.2.jpg")
    case51=pygame.image.load("Case5.1.jpg")
    case52=pygame.image.load("Case5.2.jpg")
    exit1=pygame.image.load("button_exit1.jpg")
    exit2=pygame.image.load("button_exit2.jpg")
    next1=pygame.image.load("button_next1.jpg")
    next2=pygame.image.load("button_next2.jpg")
    
    def __init__(self):
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
        
    def update(self,screen):  
        self.Bus1.drawpoint(screen)
        self.element1.update(screen,1)
        self.element2.update(screen,1)
        
    def createSprite(self,x,y,adr):
        s1 = pygame.sprite.Sprite()
        s1.image = pygame.image.load(adr).convert_alpha()
        s1.rect = s1.image.get_rect()
        (s1.rect.left, s1.rect.top) = (x,y)
        return s1   
    
    def createPalette(self):
        self.case1=self.createSprite(10,40,"Case1.1.jpg")
        self.case2=self.createSprite(self.case1.rect.left,self.case1.rect.bottom+20,"Case2.1.jpg")
        self.case3=self.createSprite(self.case2.rect.left,self.case2.rect.bottom+20,"Case3.1.jpg")
        self.case4=self.createSprite(self.case3.rect.left,self.case3.rect.bottom+20,"Case4.1.jpg")
        self.case5=self.createSprite(self.case4.rect.left,self.case4.rect.bottom+20,"Case5.1.jpg")
        self.button_exit=self.createSprite(1200, 5,"button_exit1.jpg")
        self.button_next=self.createSprite(1200, 670,"button_next1.jpg")
        
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
            if(Case1Pressed or Case2Pressed or Case3Pressed or Case4Pressed or Case5Pressed):
                self.update(screen)
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
    
           
