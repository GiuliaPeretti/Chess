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

    def set_pos(self, row, col):
        print('set in piece')

        self.row=row
        self.col=col

    def move(self, row, col, win, path):
        print('move in piece')

        self.set_pos(row, col)
        self.draw(win, path)

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
        super().draw(win, self.get_path())

    def get_path(self):
        if self.color==0:
            path="Icons/black/pawn.png"
        else:
            path="Icons/white/pawn.png"
        return path

    def move(self, row, col, win):
        super().move(row, col, win, self.get_path())

class Rook(Piece):
    def __init__(self, row, col, color):
        super().__init__(row,col)
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

    def draw(self, win):
        super().draw(win, self.get_path())

    def get_path(self):
        if self.color==0:
            path="Icons/black/rook.png"
        else:
            path="Icons/white/rook.png"
        return path

    def move(self, row, col, win):
        print('move in rook')
        super().move(row, col, win, self.get_path())

 

class Bishop(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col)
        self.color=color
    
    def valid_moves(self, board):
        valid_moves=[]
        free=True
        c=1
        while(free):
            if self.row+c>=8 or self.col+c>=8 or board[self.row+c][self.col+c] is not None:
                free=False
            else:
                valid_moves.append((self.row+c, self.col+c))
            c+=1

        free=True
        c=1
        while(free):
            if self.row-c<0 or self.col-c<0 or board[self.row-c][self.col-c] is not None:
                free=False
            else:
                valid_moves.append((self.row-c, self.col-c))
            c+=1

    
        free=True
        c=1
        while(free):
            if self.row+c<0 or self.col-c<0 or board[self.row+c][self.col-c] is not None:
                free=False
            else:
                valid_moves.append((self.row+c, self.col-c))
            c+=1

        free=True
        c=1
        while(free):
            if self.row-c<0 or self.col+c<0 or board[self.row-c][self.col+c] is not None:
                free=False
            else:
                valid_moves.append((self.row-c, self.col+c))
            c+=1

        return(valid_moves)

    def draw(self, win):
        super().draw(win, self.get_path())

    def get_path(self):
        if self.color==0:
            path="Icons/black/bishop.png"
        else:
            path="Icons/white/bishop.png"
        return path

    def move(self, row, col, win):
        super().move(row, col, win, self.get_path())


class Knight(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col)
        self.color=color
    
    def valid_moves(self, board):
        valid_moves=[]
        pos=[(self.row-2, self.col+1),(self.row-2, self.col-1),
             (self.row+2, self.col+1),(self.row+2, self.col-1),
             (self.row-1, self.col-2),(self.row+1, self.col-2),
             (self.row-1, self.col+2),(self.row+1, self.col+2)]
        
        for p in pos:
            if p[0]>=0 and p[0]<8 and p[1]>=0 and p[1]<8 and board[p[0]][p[1]] is None:
                valid_moves.append((p[0],p[1]))
        return valid_moves

    def draw(self, win):
        super().draw(win, self.get_path())

    def get_path(self):
        if self.color==0:
            path="Icons/black/knight.png"
        else:
            path="Icons/white/knight.png"
        return path

    def move(self, row, col, win):
        super().move(row, col, win, self.get_path())


class Queen(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col)
        self.color=color
    
    def valid_moves(self, board):
        valid_moves=[]
        free=True
        c=1
        while(free):
            if self.row+c>=8 or self.col+c>=8 or board[self.row+c][self.col+c] is not None:
                free=False
            else:
                valid_moves.append((self.row+c, self.col+c))
            c+=1

        free=True
        c=1
        while(free):
            if self.row-c<0 or self.col-c<0 or board[self.row-c][self.col-c] is not None:
                free=False
            else:
                valid_moves.append((self.row-c, self.col-c))
            c+=1

    
        free=True
        c=1
        while(free):
            if self.row+c<0 or self.col-c<0 or board[self.row+c][self.col-c] is not None:
                free=False
            else:
                valid_moves.append((self.row+c, self.col-c))
            c+=1

        free=True
        c=1
        while(free):
            if self.row-c<0 or self.col+c<0 or board[self.row-c][self.col+c] is not None:
                free=False
            else:
                valid_moves.append((self.row-c, self.col+c))
            c+=1

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
    
    def draw(self, win):
        super().draw(win, self.get_path())

    def get_path(self):
        if self.color==0:
            path="Icons/black/queen.png"
        else:
            path="Icons/white/queen.png"
        return path

    def move(self, row, col, win):
        super().move(row, col, win, self.get_path())

class King(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col)
        self.color=color
    
    def valid_moves(self, board):
        valid_moves=[]

        pos=[(self.row-1, self.col-1),(self.row-1, self.col), (self.row-1, self.col+1),
             (self.row, self.col-1), (self.row, self.col+1),
             (self.row+1, self.col-1),(self.row+1, self.col),(self.row+1, self.col+1)]
        
        for p in pos:
            if p[0]>=0 and p[0]<8 and p[1]>=0 and p[1]<8 and board[p[0]][p[1]] is None:
                valid_moves.append((p[0],p[1]))
        return valid_moves

    def draw(self, win):
        super().draw(win, self.get_path())

    def get_path(self):
        if self.color==0:
            path="Icons/black/king.png"
        else:
            path="Icons/white/king.png"
        return path

    def move(self, row, col, win):
        super().move(row, col, win, self.get_path())