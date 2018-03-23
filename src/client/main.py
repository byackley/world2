import pygame

XSIZE = 320
YSIZE = 240
SCALE = 2

running = True

pygame.init()
screen = pygame.set_mode( (XSIZE*SCALE, YSIZE*SCALE) )
back = pygame.Surface(XSIZE * YSIZE)

def update():
    global running
    running = False

def render():
    pass

while running:
    update()
    render()
    
