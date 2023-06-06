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
    levl_menu = text.render("Ваш максимальный уровень:" + str(int(model.level_2)), True, [0, 200, 0, ], [0, 0, 100])
    window.blit(levl_menu,[(800-levl_menu.get_width()),30])
    display.flip()
    print(model.level_2)

window = display.set_mode([800, 800])