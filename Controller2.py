import model, pygame


def controller():
    event = pygame.event.get()
    for cobitie in event:

        if cobitie.type==pygame.QUIT:
            exit()

        if cobitie.type==pygame.KEYDOWN and cobitie.key==pygame.K_SPACE:
            model.octaloc_ottalk=5
            model.px_y=3
            model.px_x=-5
            model.slid="game"

