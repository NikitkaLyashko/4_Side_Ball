import pygame.display

import model
from pygame import display
pygame.init()
text = pygame.font.SysFont("arial", 30, False, True)

def background():

    window.fill([255,125,225])
    # pygame.draw.rect(window,[225,0,0],model.rect)
    pygame.draw.circle(window, [0,225,0], model.rect_ball.center, 35)
    pygame.draw.rect(window,[0,0,0],model.rect_plat)

    text_on_wind = text.render("Осталось отталкиваний:"+str(model.octaloc_ottalk), True, [134, 213, 42])
    window.blit(text_on_wind, [800-text_on_wind.get_width(), 30])





    display.flip()

window = display.set_mode([800, 800])
