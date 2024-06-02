from re import S
import tkinter as tk
from tkinter import messagebox
import random

from Arbol import ARBOL

class TotitoBoard:
    def __init__(self, root, arbol):
        self.root = root
        self.root.title("Totito")
        self.root.geometry("530x600")
        
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.arbol=ARBOL()
        self.arbol=arbol
        self.create_board()
        
    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=('normal', 40, 'bold'), width=5, height=2, command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
        
        self.reset_button = tk.Button(self.root, text="Reiniciar", font=('normal', 14), command=self.reset_board)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")
        
        self.labelName = tk.Label(self.root, text="Edwin Adony Montejo Martinez \n 9490-21-3898", font=('normal', 14))
        self.labelName.grid(row=4, column=0, columnspan=4, sticky="nsew")

    
    def on_button_click(self, index):
        if self.buttons[index]["text"] == "" and self.check_winner() is False:
            self.buttons[index]["text"] = self.current_player
            self.board[index] = self.current_player
            index=index+1
            if self.arbol.avanzar(index)==0:
                self.arbol.insert(index,index)
            if self.check_winner():
                self.arbol.asignarValores(False)
                messagebox.showinfo("Fin del juego", f"El jugador {self.current_player} gana!")
            elif "" not in self.board:
                self.arbol.asignarValores()
                messagebox.showinfo("Fin del juego", "Es un empate!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.computer_move()
    
    def computer_move(self):
        available_moves = [i for i, x in enumerate(self.board) if x == ""]
        if available_moves:
            index = self.arbol.buscaOpc()
            self.buttons[index-1]["text"] = self.current_player
            self.board[index-1] = self.current_player
            if self.arbol.avanzar(index)==0:
                self.arbol.insert(index,index)
            if self.check_winner():
                self.arbol.asignarValores(True)
                messagebox.showinfo("Fin del juego", f"El jugador {self.current_player} gana!")
            elif "" not in self.board:
                self.arbol.asignarValores()
                messagebox.showinfo("Fin del juego", "Es un empate!")
            else:
                self.current_player = "X"
    
    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False
    
    def reset_board(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.arbol.ubicacion=self.arbol.raiz
        for button in self.buttons:
            button["text"] = ""
