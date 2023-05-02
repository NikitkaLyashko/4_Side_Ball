import pygame

rect=pygame.Rect(300,300,70,70)

px=3
def drive_rect():
    global px


    rect.bottom+=px

    if rect.bottom>=600:
        rect.bottom=600
        px=-3

    if rect.top<=0:
        rect.top=0
        px=-px



