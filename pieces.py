import pygame
from settings import *


class Piece:
    def __init__(self, row, col):
        self.row=row
        self.col=col

    def draw(self, win, path):
        img = pygame.image.load(path)
        img=pygame.transform.scale(img, (CELL_SIZE-5,CELL_SIZE-5))
        # imagerect = img.get_rect()
        win.blit(img, (self.col*75+22,self.row*CELL_SIZE+SCREEN_BORDER+2))
    
    def draw_valid(self, win, valid_moves):
        for v in valid_moves:
            if (v[0]%2==0 and v[1]%2==0 or v[0]%2!=0 and v[1]%2!=0):
                color=DARK_GREEN
            else:
                color=LIGHT_GREEN
            pygame.draw.rect(win, color, (v[1]*CELL_SIZE+SCREEN_BORDER, v[0]*CELL_SIZE+SCREEN_BORDER, CELL_SIZE, CELL_SIZE ))


class Pawn(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col)
        self.color=color
    
    def valid_moves(self, board):
        valids=[]
        if self.color==0:
            if(self.row+1<=8 and board[self.row+1][self.col] is None):
                valids.append((self.row+1,self.col))
            if(self.row+2<=8 and board[self.row+2][self.col] is None):
                valids.append((self.row+2,self.col))   
        #TODO: add en passant
        else:
            if(self.row-1<=8 and board[self.row-1][self.col] is None):
                valids.append((self.row-1,self.col))
            if(self.row-2<=8 and board[self.row-2][self.col] is None):
                valids.append((self.row-2,self.col)) 
        return(valids)


    def draw(self, win):
        if self.color==0:
            path="Icons/black/pawn.png"
        else:
            path="Icons/white/pawn.png"
        super().draw(win, path)

class Rook:
    def __init__(self, row, col, color):
        self.row=row
        self.col=col
        self.color=color
    
    def valid_moves(self, board):
        valid_moves=[]
        free=True
        c=1
        while(free):
            if self.row+c>=8 or board[self.row+c][self.col] is not None:
                free=False
            else:
                valid_moves.append((self.row+c, self.col))
            c+=1

        free=True
        c=1
        while(free):
            if self.row-c<0 or board[self.row-c][self.col] is not None:
                free=False
            else:
                valid_moves.append((self.row-c, self.col))
            c+=1

        free=True
        c=1
        while(free):
            if self.col+c>=8 or board[self.row][self.col+c] is not None:
                free=False
            else:
                valid_moves.append((self.row, self.col+c))
            c+=1

        free=True
        c=1
        while(free):
            if self.col-c<0 or board[self.row][self.col-c] is not None:
                free=False
            else:
                valid_moves.append((self.row, self.col-c))
            c+=1
        return(valid_moves)
    
    def draw_valid(self, win, valid_moves):
        for v in valid_moves:
            if (v[0]%2==0 and v[1]%2==0 or v[0]%2!=0 and v[1]%2!=0):
                color=DARK_GREEN
            else:
                color=LIGHT_GREEN
            pygame.draw.rect(win, color, (v[1]*CELL_SIZE+SCREEN_BORDER, v[0]*CELL_SIZE+SCREEN_BORDER, CELL_SIZE, CELL_SIZE ))


    def draw(self, win):
        if self.color==0:
            img = pygame.image.load("Icons/black/rook.png")
        else:
            img = pygame.image.load("Icons/white/rook.png")
        img=pygame.transform.scale(img, (CELL_SIZE-5,CELL_SIZE-5))
        # imagerect = img.get_rect()
        win.blit(img, (self.col*75+22,self.row*CELL_SIZE+SCREEN_BORDER+2))