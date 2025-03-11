import pygame as pg 
import os

pg.init()
im = pg.image.load('Playr.png') 
screen = pg.display.set_mode((700,700))
pg.mixer.init()
i = 0
run = True
paused = False
while run:
    screen.blit(im,(0,0))
    pg.display.update()
    for e in pg.event.get():
        if e.type == pg.KEYDOWN and e.key == pg.K_KP_ENTER:
             pg.mixer.music.load(f'sound\\{os.listdir('sound')[i]}')
             pg.mixer.music.play()
        elif e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
             if not paused:
                pg.mixer.music.pause()
                paused = True
             else:
                 pg.mixer.music.unpause()
                 paused = False 
        elif e.type == pg.KEYDOWN and e.key == pg.K_RIGHT:
            pg.mixer.music.stop()
            if i < len(os.listdir('sound'))-1:
                i+=1
            else:
                i = 0
        elif e.type == pg.KEYDOWN and e.key == pg.K_LEFT:
            pg.mixer.music.stop()
            if i > 0:
                i-=1
            else:
                i = len(os.listdir('sound'))-1            
        elif e.type == pg.QUIT: 
            run = False
