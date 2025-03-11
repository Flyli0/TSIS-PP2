import pygame as pg

pg.init()
screen = pg.display.set_mode((700,700))
run = True
x = 350
y = 350
while run:
    keys = pg.key.get_pressed()
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False 
    if keys[pg.K_RIGHT]:
        if x+25 < 681:
            x+=20
        else:
            x+=700 - (x+20)
    if keys[pg.K_LEFT]:
        if x-25 > 19:
            x-=20
        else:
            x-=(x-20)
    if keys[pg.K_UP]:
        if y-25 > 19:
            y-=20
        else:
            y-=(y-20)
    if keys[pg.K_DOWN]:
        if y+25 < 681:
            y+=20
        else:
            y+=700 - (y+20)
    screen.fill((255,255,255))
    a = pg.draw.circle(screen,(100,255,100),(x,y),25)
    pg.time.delay(20)
    pg.display.update()