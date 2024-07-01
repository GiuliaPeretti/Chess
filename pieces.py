import pygame

class Pawn:
    def __init__(self, row, col, color):
        self.row=row
        self.col=col
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
    
    def draw(self, win):
        img = pygame.image.load("Icons/black/pawn.png")
        imagerect = img.get_rect()
        win.blit(img, imagerect)