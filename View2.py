import pygame.display

import model
from pygame import display
pygame.init()
text = pygame.font.SysFont("arial", 30, False, True)
menu_picture=pygame.image.load("Mene Picture.jpg")
picture_2 = pygame.transform.scale(menu_picture, [800, 800])
text_menu = text.render("Нажми на пробел, чтобы запустить игру.", True, [0, 200, 0, ], [0, 0, 100])
def background():
    window.blit(picture_2,[0,0])
    window.blit(text_menu,[(800-text_menu.get_width())/2, 400])
    display.flip()


window = display.set_mode([800, 800])