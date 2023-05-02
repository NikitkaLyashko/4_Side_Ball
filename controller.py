import model, pygame


def controller():
    event = pygame.event.get()
    for cobitie in event:

        if cobitie.type==pygame.QUIT:
            exit()


