import sys

import pygame

## https://www.chess.com/dyngenerated/active-theme-css?board_size=200&pieces_size=150&visitor=1
## actual chess.com resources ^^^

# initialise pygame
pygame.init()

# set screen settings
x = 400 # inefficient, change later on
screen = pygame.display.set_mode((x, x))
pygame.display.set_caption("btec chess.com")

# set colors
WHITE = (235, 236, 208)
BLACK = (115, 149, 82)

# Main loop
running = True
while running:


    screen.fill(WHITE)


    # pygame.draw.rect(surface, colour, rect)
    # rect syntax: (position, dimensions)

    len = x // 8 # sidelength of a square

## 13/11/2024
    # algorithm that creates 'checkerboard' pattern
    for j in range(4):
        for i in range(4):
            pygame.draw.rect(screen, BLACK, ((len + (len * i * 2), 0 + \
                                              (len * j * 2)), (len, len)))
    for j in range(4):
        for i in range(4):
            pygame.draw.rect(screen, BLACK, ((0 + (len * i * 2), len + \
                                              (len * j * 2)), (len, len)))

## 20/11/2024
    ## https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame

    whitePawn = pygame.image.load('Pieces/White/wp.png')
    whitePawn = pygame.transform.scale(whitePawn, (len, len)) #

    class Piece:
          def __init__(self, type, colour, position, sprite):
            self.type = type
            self.colour = colour
            self.position = position
            self.sprite = sprite

          def place(self, screen, square):
            x, y = self.position # tuple
            screen.blit(self.type, (x * square, y * square))

    image = pygame.Surface((50, 50))
    image.fill((255, 255, 255))
    
    pawn = Piece(type = "pawn", colour = "white", position = (1, 2), \
                 sprite = image)
    
    pawn.place(screen, x // 8)

    ## PAWN
    # for pawn in range(8): # screen.blit(whitePawn, (0, y - len * 2))
    #     screen.blit(whitePawn, (0 + len * pawn, x - len * 2))



    ## https://www.pygame.org/docs/tut/MoveIt.html
    # teaches pygame basics ^^^

    ## https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs

    takes = pygame.mixer.Sound('capture.wav')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            takes.play()

    # update display
    pygame.display.flip()

# quit pygame
pygame.quit()
sys.exit()