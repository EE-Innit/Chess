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
    whiteKing = pygame.image.load('Pieces/White/wk.png')
    whiteKing = pygame.transform.scale(whiteKing, (len, len)) # could improve

    whiteQueen = pygame.image.load('Pieces/White/wq.png')
    whiteQueen = pygame.transform.scale(whiteQueen, (len, len)) #
    
    whitePawn = pygame.image.load('Pieces/White/wp.png')
    whitePawn = pygame.transform.scale(whitePawn, (len, len)) #

    whiteKnight = pygame.image.load('Pieces/White/wn.png')
    whiteKnight = pygame.transform.scale(whiteKnight, (len, len)) #

    whiteBishop = pygame.image.load('Pieces/White/wb.png')
    whiteBishop = pygame.transform.scale(whiteBishop, (len, len)) #
    
    whiteRook = pygame.image.load('Pieces/White/wr.png')
    whiteRook = pygame.transform.scale(whiteRook, (len, len)) #



    
    # .blit() syntax: object, x, y
    
    ### WHITE
    ## PAWN
    for pawn in range(8): # screen.blit(whitePawn, (0, y - len * 2))
        screen.blit(whitePawn, (0 + len * pawn, x - len * 2))

    ## MINOR PIECES
    screen.blit(whiteKnight, (len, x - len))
    screen.blit(whiteKnight, (len * 6, x - len))

    screen.blit(whiteBishop, (len * 2, x - len)) # dark-squared bishop
    screen.blit(whiteBishop, (len * 5, x - len)) # light-squared bishop
    
    ## MAJOR PIECES
    screen.blit(whiteRook, (0, x - len))
    screen.blit(whiteRook, (len * 7, x - len))

    screen.blit(whiteQueen, (len * 3, x - len))
    screen.blit(whiteKing, (len * 4, x - len))
    
    ### BLACK
    ## PAWN
    for pawn in range(8):
        screen.blit(whitePawn, (0 + len * pawn, x - len * 2))

    ## MINOR PIECES
    screen.blit(whiteKnight, (len, x - len))
    screen.blit(whiteKnight, (len * 6, x - len))

    screen.blit(whiteBishop, (len * 2, x - len)) # dark-squared bishop
    screen.blit(whiteBishop, (len * 5, x - len)) # light-squared bishop

    ## MAJOR PIECES
    screen.blit(whiteRook, (0, x - len))
    screen.blit(whiteRook, (len * 7, x - len))

    screen.blit(whiteQueen, (len * 3, x - len))
    screen.blit(whiteKing, (len * 4, x - len))

    
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