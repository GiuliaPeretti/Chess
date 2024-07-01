import pygame
from settings import *
from pieces import *

#TODO: arrocchi
#TODO: promozione pedoni
#TODO: condizione scacco
#TODO: scacco matto
#TODO: stallo
#TODO: tempo
#

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

    board[0]=[Rook(0,0,0), Knight(0,1,0), Bishop(0,2,0), Queen(0,3,0), King(0,4,0), Bishop(0,5,0), Knight(0,6,0), Rook(0,7,0)]
    board[1]=[Pawn(1,0,0), Pawn(1,1,0), Pawn(1,2,0), Pawn(1,3,0), Pawn(1,4,0), Pawn(1,5,0), Pawn(1,6,0), Pawn(1,7,0)]
    board[6]=[Pawn(6,0,1), Pawn(6,1,1), Pawn(6,2,1), Pawn(6,3,1), Pawn(6,4,1), Pawn(6,5,1), Pawn(6,6,1), Pawn(6,7,1)]
    board[7]=[Rook(7,0,1), Knight(7,1,1), Bishop(7,2,1), Queen(7,3,1), King(7,4,1), Bishop(7,5,1), Knight(7,6,1), Rook(7,7,1)]

    return(board)

def handle_mouse_input(x,y):
    global selected
    row=(y-SCREEN_BORDER)//CELL_SIZE
    col=(x-SCREEN_BORDER)//CELL_SIZE
    if selected is None:
        draw_chessboard()
        draw_board()
        if board[row][col] is not None:
            valids=board[row][col].valid_moves(board)
            board[row][col].draw_valid(screen,valids)
        selected=(row,col)
        draw_board()
    else:
        valids=board[selected[0]][selected[1]].valid_moves(board)
        if (row,col) in valids:
            move(row, col, selected)
        selected=None
        draw_chessboard()
        draw_board()


def draw_board():
    for row in board:
        for cell in row:
            if cell is not None:
                cell.draw(screen)

def move(row, col, selected):
    board[selected[0]][selected[1]].move(row,col,screen)
    board[row][col]=board[selected[0]][selected[1]]
    board[selected[0]][selected[1]]=None

def get_white_king():
    for row in range(len(board)):
        for col in range(len(board[row])):
            if isinstance(board[row][col], King) and board[row][col].get_color()==1:
                return(row,col)

def get_balck_king():
    for row in range(len(board)):
        for col in range(len(board[row])):
            if isinstance(board[row][col], King) and board[row][col].get_color()==0:
                return(row,col)



if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption("Chess♥")
    run = True
    win=False
    clock=pygame.time.Clock()


    selected=None


    draw_background()
    draw_chessboard()
    board=gen_board()
    draw_board()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                handle_mouse_input(x, y)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()