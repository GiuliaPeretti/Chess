import pygame
from settings import *
from pieces import *

def draw_background():
    screen.fill(BACKGROUND_COLOR)

def draw_chessboard():
    for row in range (8):
        for col in range(8):
            if (row%2==0 and col%2==0 or row%2!=0 and col%2!=0):
                color=DARK_PINK
            else:
                color=LIGHT_PINK
            pygame.draw.rect(screen, color, (col*CELL_SIZE+SCREEN_BORDER, row*CELL_SIZE+SCREEN_BORDER, CELL_SIZE, CELL_SIZE))
        
def gen_board():
    board=[]
    for i in range(8):
        t=[]
        for j in range(8):
            t.append(None)
        board.append(t)
    return(board)



if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption("Chess♥")
    run = True
    win=False
    clock=pygame.time.Clock()

    draw_background()
    draw_chessboard()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()