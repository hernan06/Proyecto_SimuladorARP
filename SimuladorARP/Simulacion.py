'''
Created on 13/01/2013

@author: Hernan
'''
import pygame
import random
from Host import Host
from Router import Router
from Bus import Bus
from ARP_request import ARP_request
from ARP_reply import ARP_reply 
from Ping import Ping

class Simulacion():
    
    def __init__(self):
        self.element1=None
        self.element2=None
        self.element3=None
        self.element4=None
        self.button_exit=None
        self.button_clear=None
        self.arp_request=None
        self.arp_request2=None
        self.arp_repply=None
        self.Bus1=None
        self.Bus2=None
        self.panel=None
        self.ping=None
        self.ping2=None
        self.panelList=[]
        self.exit1=pygame.image.load("Images/button_back1.jpg")
        self.exit2=pygame.image.load("Images/button_back2.jpg")
        self.clear1=pygame.image.load("Images/button_clear1.jpg")
        self.clear2=pygame.image.load("Images/button_clear2.jpg")
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
        
    def createCase5(self):
        self.element1=Host(50,200,"192.168.1.1",self.randomMAC())
        self.element2=Host(800,200,"192.168.2.2",self.randomMAC())
        self.element3=Router(450,200,"192.168.1.2",self.randomMAC())
        self.element3.insert("192.168.2.1",self.randomMAC())
        self.element3.insert("192.168.3.1",self.randomMAC())
        self.element4=Host(450,500,"192.168.3.2",self.randomMAC())
        self.Bus1=Bus(50,205,800,205)
        self.Bus2=Bus(452,200,452,500)
        self.button_exit=self.createSprite(1200, 5,"Images/button_back1.jpg")
        self.button_clear=self.createSprite(1180, 670,"Images/button_clear1.jpg")
        self.panel=self.createSprite(1000, 200,"Images/panel.jpg")
        
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
        self.Bus1=Bus(100,205,700,205)
        self.button_exit=self.createSprite(1200, 5,"Images/button_back1.jpg")
        self.button_clear=self.createSprite(1180, 670,"Images/button_clear1.jpg")
        self.panel=self.createSprite(1000, 200,"Images/panel.jpg")
        
    def printPanel(self,screen):
        pos=0
        for register in self.panelList:
            print register
            print pos
            pos=pos+1
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
    
    def update5(self,screen):
        self.Bus1.drawpoint(self.display)
        self.Bus2.drawpoint(self.display)
        self.element1.update(screen,0)
        self.element2.update(screen,0)
        self.element3.update(screen,0)
        self.element4.update(screen,0)
        self.display.blit(self.panel.image,self.panel.rect)
        self.display.blit(self.button_exit.image,self.button_exit.rect)
        self.display.blit(self.button_clear.image,self.button_clear.rect)
        self.printPanel(screen)
    
    def Selection(self,screen):
        c1 = pygame.time.Clock()
        flag=True
        flagSource=0
        flagDestination=0
        while True and flag and (flagSource==0 or flagDestination==0):
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if(self.button_exit.rect.collidepoint(x,y)):
                        flag=False
                    if(self.button_clear.rect.collidepoint(x,y)):
                        flagSource=0
                        flagDestination=0
                        self.panelList=[]
                    if events.button == 1: 
                        if self.element1.rect.collidepoint(x,y):
                            if(flagSource!=0):
                                self.panelList.pop(0)
                            flagSource=1
                            self.panelList.insert(0,[self.element1.adressIP,self.element1.adressMac,1])
                        if self.element2.rect.collidepoint(x,y):
                            if(flagSource!=0):
                                self.panelList.pop(0)
                            flagSource=2
                            self.panelList.insert(0,[self.element2.adressIP,self.element2.adressMac,1])
                        if self.element4.rect.collidepoint(x,y):
                            if(flagSource!=0):
                                self.panelList.pop(0)
                            flagSource=3
                            self.panelList.insert(0,[self.element4.adressIP,self.element4.adressMac,1])
                    if events.button == 3: 
                        if self.element1.rect.collidepoint(x,y) and flagSource!=1:
                            if(flagDestination!=0):
                                try:
                                    self.panelList.pop(0)
                                except IndexError, e:
                                    print e# or pass, do nothing just ignore that row...
                            flagDestination=1
                            self.panelList.insert(0,[self.element1.adressIP,self.element1.adressMac,2])
                        if self.element2.rect.collidepoint(x,y) and flagSource!=2:
                            if(flagDestination!=0):
                                try:
                                    self.panelList.pop(0)
                                except IndexError, e:
                                    print e# or pass, do nothing just ignore that row...
                            flagDestination=2
                            self.panelList.insert(0,[self.element2.adressIP,self.element2.adressMac,2])
                        if self.element4.rect.collidepoint(x,y) and flagSource!=3:
                            if(flagDestination!=0):
                                try:
                                    self.panelList.pop(0)
                                except IndexError, e:
                                    print e# or pass, do nothing just ignore that row...
                            flagDestination=3
                            self.panelList.insert(0,[self.element4.adressIP,self.element4.adressMac,2])
            c1.tick(100)
            screen.fill((255,255,255))
            self.update5(screen)
            pygame.display.update()
        return self.ARPHostToRouter(flagSource, flagDestination, screen,flag)
        
    def CreateARPrequest(self,flagSource):
        if(flagSource==1):
            self.arp_request=ARP_request(self.element1.rect.right,self.element1.rect.top,self.element1,self.element3)
            return 1
        if(flagSource==2):
            self.arp_request=ARP_request(self.element2.rect.left,self.element2.rect.top,self.element2,self.element3)
            return 2
        if(flagSource==3):
            self.arp_request=ARP_request(self.element4.rect.left,self.element4.rect.top,self.element4,self.element3)
            return 3
        
    def CreateARPreply(self,flagDestination,dir):
        self.arp_repply=ARP_reply(self.element3.rect.left,self.element3.rect.top,self.element3,self.element3)
        if(dir==1):
            return 2
        if(dir==2):
            return 1
        return 3
    
    def CreateARPreply2(self,flagDestination):
        if(flagDestination==1):
            self.arp_repply=ARP_reply(self.element1.rect.left,self.element1.rect.top,self.element1,self.element3)
            return 1
        if(flagDestination==2):
            self.arp_repply=ARP_reply(self.element2.rect.left,self.element2.rect.top,self.element2,self.element3)
            return 2
        if(flagDestination==3):
            self.arp_repply=ARP_reply(self.element4.rect.left,self.element4.rect.top,self.element4,self.element3)  
            return 4  
         
    def ARPHostToRouter(self,flagSource,flagDestination,screen,flag):
        pygame.mouse.set_visible(False)
        c1 = pygame.time.Clock()
        dir=self.CreateARPrequest(flagSource)
        dir2=self.CreateARPreply(flagDestination,dir)
        insert=0
        flag2=True
        while True and flag and flag2:
            pygame.mouse.set_pos([0,0])
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if(self.button_exit.rect.collidepoint(x,y)):
                        flag=False
            
            c1.tick(100)
            screen.fill((255,255,255))      
            if(self.arp_request.Arp_message.rect.colliderect(self.element3.rect)):
                if(insert==0):
                    self.element3.insert(self.arp_request.ipSource,self.arp_request.macSource)
                    insert=1
                if(self.Colision(flagSource,flagDestination)):
                    flag=True
                    flag2=False
                else:
                    self.arp_repply.MoveARP(dir2)
                    self.arp_repply.update(screen)
            else:
                self.arp_request.MoveARP(dir)
                self.arp_request.update(screen)
            self.update5(screen)
            pygame.display.update()
        return self.ARPRouterToHost(flagSource, flagDestination, screen,flag)
    
    def ARPHostToRouter2(self,flagSource,flagDestination,screen,flag):
        pygame.mouse.set_visible(False)
        c1 = pygame.time.Clock()
        dir=self.CreateARPrequest(flagDestination)
        dir2=self.CreateARPreply(flagSource,dir)
        insert=0
        flag2=True
        while True and flag and flag2:
            pygame.mouse.set_pos([0,0])
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if(self.button_exit.rect.collidepoint(x,y)):
                        flag=False
            
            c1.tick(100)
            screen.fill((255,255,255))      
            if(self.arp_request.Arp_message.rect.colliderect(self.element3.rect)):
                if(insert==0):
                    self.element3.insert(self.arp_request.ipSource,self.arp_request.macSource)
                    insert=1
                if(self.Colision(flagDestination,flagSource)):
                    flag=True
                    flag2=False
                else:
                    self.arp_repply.MoveARP(dir2)
                    self.arp_repply.update(screen)
            else:
                self.arp_request.MoveARP(dir)
                self.arp_request.update(screen)
            self.update5(screen)
            pygame.display.update()
        pygame.mouse.set_visible(True)
        return flag    
    
    def ARPRouterToHost(self,flagSource,flagDestination,screen,flag):
        pygame.mouse.set_visible(False)
        c1 = pygame.time.Clock()
        flag2=True
        if(flagSource==1):
            dir=1
            dir2=4
            self.ping=Ping(self.element1.rect.left,self.element1.rect.top)
        if(flagSource==2):
            dir=2
            dir2=4
            self.ping=Ping(self.element2.rect.left,self.element2.rect.top)
        if(flagSource==3):
            dir=1
            dir2=2
            self.ping=Ping(self.element4.rect.left,self.element4.rect.top)
        self.arp_request=ARP_request(self.element3.rect.left,self.element3.rect.top,self.element3,self.element1)
        self.arp_request2=ARP_request(self.element3.rect.left,self.element3.rect.top,self.element3,self.element2)
        dir3=self.CreateARPreply2(flagDestination)
        insert1=0
        insert2=0
        cont=0
        while True and flag and flag2:
            pygame.mouse.set_pos([0,0])
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if(self.button_exit.rect.collidepoint(x,y)):
                        flag=False
            
            c1.tick(100)
            screen.fill((255,255,255))
            if(self.ping.message.rect.colliderect(self.element3.rect)):
                cont=self.Colision2(flagSource,insert1,insert2)
                if(flagSource==1):
                    if(insert1==0 and cont==1):
                        self.Search(2)
                        insert1=1
                    if(insert2==0 and cont==2):
                        self.Search(3)
                        insert2=1   
                if(flagSource==2):
                    if(insert1==0 and cont==1):
                        self.Search(1)
                        insert1=1
                    if(insert2==0 and cont==2):
                        self.Search(3)
                        insert2=1
                if(flagSource==3):
                    if(insert1==0 and cont==1):
                        self.Search(2)
                        insert1=1
                    if(insert2==0 and cont==2):
                        self.Search(1)
                        insert2=1   
                if(insert1==1 and insert2==1):
                    if(self.arp_repply.Arp_message.rect.colliderect(self.element3.rect)):
                        self.element3.insert(self.arp_repply.ipSource,self.arp_repply.macSource)
                        flag=True
                        flag2=False
                    else:
                        self.arp_repply.MoveARP(dir3)
                        self.arp_repply.update(screen)
                else:
                    if(insert1==0):
                        self.arp_request.MoveARP(dir)
                        self.arp_request.update(screen)
                    if(insert2==0):
                        self.arp_request2.MoveARP(dir2)
                        self.arp_request2.update(screen)
            else:
                self.ping.MovePing(flagSource)
                self.ping.update(screen)
            self.update5(screen)
            pygame.display.update()
        return self.ARPping(flagSource, flagDestination, screen,flag)
    
    def ARPping(self,flagSource,flagDestination,screen,flag):
        pygame.mouse.set_visible(False)
        c1 = pygame.time.Clock()
        flag2=True
        if(flagSource==1):
            self.ping=Ping(self.element1.rect.left,self.element1.rect.top)
        if(flagSource==2):
            self.ping=Ping(self.element2.rect.left,self.element2.rect.top)
        if(flagSource==3):
            self.ping=Ping(self.element4.rect.left,self.element4.rect.top)
        self.ping2=Ping(self.element3.rect.left,self.element3.rect.top)
        while True and flag and flag2:
            pygame.mouse.set_pos([0,0])
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if(self.button_exit.rect.collidepoint(x,y)):
                        flag=False
            
            c1.tick(100)
            screen.fill((255,255,255))
            if(self.ping.message.rect.colliderect(self.element3.rect)):
                if(flagDestination==1):
                    if(self.ping2.message.rect.colliderect(self.element1.rect)):
                        flag=True
                        flag2=False
                    else:
                        self.ping2.MovePing(2)
                        self.ping2.update(screen)
                if(flagDestination==2):
                    if(self.ping2.message.rect.colliderect(self.element2.rect)):
                        flag=True
                        flag2=False
                    else:
                        self.ping2.MovePing(1)
                        self.ping2.update(screen)
                if(flagDestination==3):
                    if(self.ping2.message.rect.colliderect(self.element4.rect)):
                        flag=True
                        flag2=False
                    else:
                        self.ping2.MovePing(4)
                        self.ping2.update(screen)
            else:
                self.ping.MovePing(flagSource)
                self.ping.update(screen)
            self.update5(screen)
            pygame.display.update()
        return self.ARPHostToRouter2(flagSource,flagDestination, screen,flag)
        
    def Search(self,number):
        cont=1
        for register in self.element3.Ips:
            tmp=register
            if(cont==number):
                ip=tmp[0]
                mac=tmp[1]
            cont=cont+1
        if(number==1):
            self.element1.insert(ip, mac)
        if(number==2):
            self.element2.insert(ip, mac)
        if(number==3):
            self.element4.insert(ip, mac)
            
    def Colision2(self,flagSource,flag1,flag2):
        rt1=0
        rt2=0
        if(flagSource==1):
            if(self.arp_request.Arp_message.rect.colliderect(self.element2.rect) and flag1==0):
                rt1=1
            if(self.arp_request2.Arp_message.rect.colliderect(self.element4.rect) and flag2==0):
                rt2=1
        if(flagSource==2):
            if(self.arp_request.Arp_message.rect.colliderect(self.element1.rect) and flag1==0):
                rt1=1
            if(self.arp_request2.Arp_message.rect.colliderect(self.element4.rect) and flag2==0):
                rt2=1
        if(flagSource==3):
            if(self.arp_request.Arp_message.rect.colliderect(self.element2.rect) and flag1==0):
                rt1=1
            if(self.arp_request2.Arp_message.rect.colliderect(self.element1.rect) and flag2==0):
                rt2=1
        if(rt1==1):
            return 1
        if(rt2==1):
            return 2
        else:
            return 0 
     
    def Colision(self,flagSource,flagDestination): 
        cont=1
        for register in self.element3.Ips:
            tmp=register
            if(cont==flagSource):
                mac=tmp[1]
            cont=cont+1
        if(flagSource==1):
            if(self.arp_repply.Arp_message.rect.colliderect(self.element1.rect)):
                if(flagDestination==1):
                    ip=self.element1.adressIP
                if(flagDestination==2):
                    ip=self.element2.adressIP
                if(flagDestination==3):
                    ip=self.element4.adressIP
                self.element1.insert(ip,mac)
                return True
        if(flagSource==2):
            if(self.arp_repply.Arp_message.rect.colliderect(self.element2.rect)):
                if(flagDestination==1):
                    ip=self.element1.adressIP
                if(flagDestination==2):
                    ip=self.element2.adressIP
                if(flagDestination==3):
                    ip=self.element4.adressIP
                self.element2.insert(ip,mac)
                return True
        if(flagSource==3):
            if(self.arp_repply.Arp_message.rect.colliderect(self.element4.rect)):
                if(flagDestination==1):
                    ip=self.element1.adressIP
                if(flagDestination==2):
                    ip=self.element2.adressIP
                if(flagDestination==3):
                    ip=self.element4.adressIP
                self.element4.insert(ip,mac)
                return True    
        return False
           
    def ARPSimulationCase5(self,screen):
        self.createCase5()
        flag=self.Selection(screen)
        c1 = pygame.time.Clock()
        while True and flag:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if(self.button_exit.rect.collidepoint(x,y)):
                        flag=False
                    if(self.button_clear.rect.collidepoint(x,y)):
                        self.createCase5()
                        self.panelList=[]
                        flag=self.Selection(screen)
                        
            c1.tick(100)
            screen.fill((255,255,255))
            self.update5(screen)
            pygame.display.update()
        
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
        clean=0
        while True and flag:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if(self.button_exit.rect.collidepoint(x,y)):
                        flag=False
                    if(self.button_clear.rect.collidepoint(x,y)):
                        flagSource=0
                        move=0
                        SetDestination=False
                        SetSource=False
                        flag1=1
                        flagC=True
                        self.panelList=[]
                        if(clean==1):
                            self.element1.Ips.pop(1)
                            self.element2.Ips.pop(1)
                            clean=0
                    if events.button == 1: 
                        if self.element1.rect.collidepoint(x,y):
                            SetSource=True
                            x1,y1=self.element1.rect.right+2,self.element1.rect.top
                            if(flagSource!=0):
                                self.panelList.pop(0)
                            flagSource=1
                            self.panelList.append([self.element1.adressIP,self.element1.adressMac,1])
                        if self.element2.rect.collidepoint(x,y):
                            SetSource=True
                            x1,y1=self.element2.rect.left,self.element2.rect.top
                            if(flagSource!=0):
                                self.panelList.pop(0)
                            flagSource=2
                            self.panelList.append([self.element2.adressIP,self.element2.adressMac,1])
                    if events.button == 3: 
                        if self.element1.rect.collidepoint(x,y) and flagSource!=1:
                            if(SetDestination==True):
                                self.panelList.pop(0)
                            SetDestination=True
                            x2,y2=self.element1.rect.left,self.element1.rect.top
                            self.panelList.append([self.element1.adressIP,self.element1.adressMac,2])
                        if self.element2.rect.collidepoint(x,y) and flagSource!=2:
                            if(SetDestination==True):
                                self.panelList.pop(0)
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
                            clean=1
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
                            clean=1
                            self.panelList=[]
                            pygame.mouse.set_visible(True)
                            
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
        
        