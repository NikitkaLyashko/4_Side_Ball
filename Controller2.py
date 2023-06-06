import model, pygame


def controller():
    event = pygame.event.get()
    for cobitie in event:

        if cobitie.type==pygame.QUIT:
            exit()

        if cobitie.type==pygame.KEYDOWN and cobitie.key==pygame.K_SPACE:
            model.reset()
            model.slid="game"

