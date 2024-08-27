import pygame.display

import model
from pygame import display
pygame.init()
text = pygame.font.SysFont("arial", 30, False, True)
window = display.set_mode([800, 800])
def background():

    window.fill([255,125,225])
    # pygame.draw.rect(window,[225,0,0],model.rect)
    pygame.draw.circle(window, [0,225,0], model.rect_ball.center, 35)
    pygame.draw.rect(window,[0,0,0],model.rect_plat)

    text_on_wind = text.render("Осталось отталкиваний:"+str(model.octaloc_ottalk), True, [134, 213, 42])
    window.blit(text_on_wind, [800-text_on_wind.get_width(), 30])

    livs=text.render("Осталось жизней:"+str(model.oct_live),True,[134, 100, 222])
    window.blit(livs,[800-livs.get_width(),60])

    level=text.render("Уровень:"+str(model.level),True,[134, 100, 222])
    window.blit(level,[800-level.get_width(),90])






    display.flip()


