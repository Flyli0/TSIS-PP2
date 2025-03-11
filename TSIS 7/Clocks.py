import pygame as pg 
import time 

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption("Clock")
run = True
mm = pg.image.load('min.png')
mm = pg.transform.scale(mm,(70,250))
back = pg.image.load('mickeyclock.jpeg')
hh = pg.image.load('image.png')
back = pg.transform.scale(back,(500,500))
hh = pg.transform.scale(hh,(65,270))
rect = hh.get_rect(center = (250,250))
rectm = mm.get_rect(center = (250,250))
anglee = 0
anggl = 0
while run:
    a = time.localtime()
    minute = a.tm_min
    hours = a.tm_hour
    anglee = (hours / 12) * 360
    anggl = (minute/60)*360
    for e in pg.event.get():
        if e.type == pg.QUIT:
             run = False

    mmr = pg.transform.rotate(mm,-anggl)
    rrectm = mmr.get_rect(center = rectm.center)

    hhr = pg.transform.rotate(hh,-anglee)
    rrect = hhr.get_rect(center = rect.center)

    
    screen.blit(back,(0,0))
    screen.blit(mmr,rrectm.topleft)
    screen.blit(hhr,rrect.topleft)
    pg.display.update()
    anglee-=1