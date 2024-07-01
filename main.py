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

def handle_mouse_input(x,y):
    row=(y-SCREEN_BORDER)//CELL_SIZE
    col=(x-SCREEN_BORDER)//CELL_SIZE
    print(row,col)
    if board[row][col] is not None:
        valids=board[row][col].valid_moves(board)
        board[row][col].draw_valid(screen,valids)




if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption("Chess♥")
    run = True
    win=False
    clock=pygame.time.Clock()

    draw_background()
    draw_chessboard()
    board=gen_board()
    pawn = Pawn(0,0,0)
    pawn.draw(screen)
    board[0][0]=pawn

    rook = Rook(4,0,0)
    rook.draw(screen)
    board[4][0]=rook

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                handle_mouse_input(x,y)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()