import random
import math
import os

from Arbol import ARBOL

class TicTacToe:
    def __init__(self):
        self.board = ['-' for _ in range(9)]
        self.TotitoArbol=ARBOL()
        self.humanPLayer='X'
        self.botPlayer='O'
        # if random.randint(0, 1) == 1:
        #     self.humanPLayer = 'X'
        #     self.botPlayer = "O"
        # else:
        #     self.humanPLayer = "O"
        #     self.botPlayer = "X"

    def show_board(self):
        print("")
        for i in range(3):
            print("  ",self.board[0+(i*3)]," | ",self.board[1+(i*3)]," | ",self.board[2+(i*3)])
            print("")
            
    def is_board_filled(self,state):
        return not "-" in state

    def is_player_win(self,state,player):
        if state[0]==state[1]==state[2] == player: return True
        if state[3]==state[4]==state[5] == player: return True
        if state[6]==state[7]==state[8] == player: return True
        if state[0]==state[3]==state[6] == player: return True
        if state[1]==state[4]==state[7] == player: return True
        if state[2]==state[5]==state[8] == player: return True
        if state[0]==state[4]==state[8] == player: return True
        if state[2]==state[4]==state[6] == player: return True

        return False

    def checkWinner(self):
        if self.is_player_win(self.board,self.humanPLayer):
            os.system("cls")
            print(f"   Player {self.humanPLayer} wins the game!")
            self.TotitoArbol.asignarValores(False)
            return True
            
        if self.is_player_win(self.board,self.botPlayer):
            os.system("cls")
            print(f"   Player {self.botPlayer} wins the game!")
            self.TotitoArbol.asignarValores(True)
            return True

        # checking whether the game is draw or not
        if self.is_board_filled(self.board):
            os.system("cls")
            print("   Match Draw!")
            self.TotitoArbol.asignarValores()
            return True
        return False

    def start(self, Arbol):
        self.TotitoArbol=Arbol
        self.TotitoArbol.ubicacion=self.TotitoArbol.raiz
        while True:
            os.system("cls")
            print(f"   Player {self.humanPLayer} turn")
            self.show_board()
            
            #Human
            square = self.human_move()
            self.board[square] = self.humanPLayer
            if self.checkWinner():
                break
            

            #Bot
            square = self.machine_move()
            self.board[square] = self.botPlayer
            if self.checkWinner():
                break
            
        # showing the final view of board
        print()
        self.show_board()
        return self.TotitoArbol
        
    def human_move(self):
        # taking user input
        while True:
            square =  input("Enter the square to fix spot(1-9): ")
            try:
                square=int(square)
            except :
                square=0
            if square>=1 and square<=9 and not square==None:
                if self.board[square-1] == "-":
                    if self.TotitoArbol.avanzar(square)==0:
                        self.TotitoArbol.insert(square,square)
                    break
        return square-1
    
    def machine_move(self):
        while True:
            square =  int(self.TotitoArbol.buscaOpc())
            if self.board[square-1] == "-":
                if self.TotitoArbol.avanzar(square)==0:
                    self.TotitoArbol.insert(square,square)
                break
        return square-1
    
    










    
    def generarTodo(self, Arbol):
        self.TotitoArbol=Arbol
        self.TotitoArbol.ubicacion=self.TotitoArbol.raiz
        while True:
            os.system("cls")
            print(f"   Player {self.humanPLayer} turn")
            self.show_board()
            
            #Human
            square = self.machine_move_auto()
            self.board[square] = self.humanPLayer
            if self.checkWinner():
                break
            
            #Bot
            square = self.machine_move_auto()
            self.board[square] = self.botPlayer
            if self.checkWinner():
                break

        # showing the final view of board
        print()
        self.show_board()
        return self.TotitoArbol
        


    def machine_move_auto(self):
        while True:
            square =  int(self.TotitoArbol.buscaOpc())
            if self.board[square-1] == "-":
                if self.TotitoArbol.avanzar(square)==0:
                    self.TotitoArbol.insert(square,square)
                break
        return square-1
    
        # while True:
        #     square =  int(random.randint(1,9))
        #     if self.TotitoArbol.ubicacion.anterior==None:
        #         square=1
        #     if self.TotitoArbol.ubicacion.profundidad==2 and self.board[2] == "-":
        #         square=3
        #     if self.TotitoArbol.ubicacion.profundidad==4 and self.board[1] == "-":
        #         square=2
        #     if self.board[square-1] == "-":
        #         if self.TotitoArbol.avanzar(square)==0:
        #             self.TotitoArbol.insert(square,square)
        #         break
        # return square-1