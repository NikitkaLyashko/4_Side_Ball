import pygame.display

import model
from pygame import display

def background():
    window.fill([255,125,70])
    # pygame.draw.rect(window,[225,0,0],model.rect)
    pygame.draw.circle(window,[0,225,0],model.rect.center,35)






    display.flip()

window = display.set_mode([800, 600])
