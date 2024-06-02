import json
import os

import tkinter as tk
from Arbol import ARBOL
# from BoardTotito import TicTacToeBoard, TicTacToeGame
from CTotito import TicTacToe
from TotitoBoard import TotitoBoard

Arbol=ARBOL()


def configArbol():
    while True:    
        print("1. Volver a la raiz")
        print("2. ubicaciones")
        print("3. Avanzar")
        print("4. Retroceder")
        print("5. Eliminar")
        print("6. Grafica")
        print("7. Asignar Valores")
        print("0. Salir")
        opc=input("Ingrese la opcion que desea ")
        try:
            opc=int(opc)
        except :
            opc=100
        if opc==1:
            Arbol.ubicacion=Arbol.raiz
            Arbol.ubicaciones()
        elif opc==2:
            Arbol.ubicaciones()
        elif opc==3:
            try:
                Arbol.avanzar(int(input("Inserte la posicion que desea avanzar")))
                Arbol.ubicaciones()
            except :
                print("no disponible")
        elif opc==4:
            Arbol.volver()
            Arbol.ubicaciones()
        elif opc==5:
            try:
                Arbol.eliminar(int(input("Inserte la posicion que desea eliminar")))
                Arbol.ubicaciones()
            except :
                 print("no disponible")
        elif opc==6:
            Arbol.generar_arbol_grafico()
            Arbol.ubicaciones()
        elif opc==7:
            Arbol._asignarValores(Arbol.raiz)
            Arbol.ubicacion=Arbol.raiz
            Arbol.ubicaciones()
        elif opc==0:
            break

           




def opciones():
    while True:
        print("1. Juego Consola")
        print("2. Generar Pruebas")
        print("3. Generar Json")
        print("4. Consultar Json")
        print("5. Opciones Arbol")
        print("0. Salir")
        opc=input("Ingrese la opcion que desea ")
        try:
            opc=int(opc)
        except :
            opc=100
        if opc==1:
            Totito=TicTacToe()
            Totito.start(Arbol)
        elif opc==2:
            try:
                rango=int(input("Ingrese la cantidad de pruebas de Juego que desea: "))
            except :
                rango=0
            for x in range(rango):
                print(x)
                totito = TicTacToe()
                totito.generarTodo(Arbol)
        elif opc==3:
            json.dump(Arbol.generarJson(Arbol.raiz), open('arbol.json' , 'w'), indent=4)
        elif opc==4:
            Arbol.generarArbolDeJson()
        elif opc==5:
            os.system("cls")
            configArbol()
            os.system("cls")
        elif opc==0:
            break



print("Edwin Adony Montejo Martinez - 9490-21-3898")

while True:
    print("1. Jugar")
    print("2. Opciones Juego")
    print("0. Salir")
    opc=input("Ingrese la opcion que desea ")
    try:
        opc=int(opc)
    except :
        opc=100
    if opc==1:
        root = tk.Tk()
        game = TotitoBoard(root, Arbol)
        root.mainloop()
        os.system("cls")
        # game = TicTacToeGame(Arbol)
        # board = TicTacToeBoard(game)
        # board.mainloop()
    elif opc==2:
        os.system("cls")
        opciones()
        os.system("cls")
    elif opc==0:
        break

