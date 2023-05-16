import model, pygame


def controller():
    event = pygame.event.get()
    for cobitie in event:

        if cobitie.type==pygame.QUIT:
            exit()

        if cobitie.type==pygame.KEYDOWN and cobitie.key==pygame.K_d:
            model.platforma_right()

        if cobitie.type==pygame.KEYDOWN and cobitie.key==pygame.K_w:
            model.platforma_top()

        if cobitie.type==pygame.KEYDOWN and cobitie.key==pygame.K_a:
            model.platforma_left()

        if cobitie.type==pygame.KEYDOWN and cobitie.key==pygame.K_s:
            model.platforma_down()



