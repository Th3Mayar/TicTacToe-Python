#Proyecto: Pizarra Tic Toc (Un tablero de tres en raya)

import os
from ast import main
from random import *
import time

Diccionario = {

    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '

    }

def fTabla(Diccionario):
    print("\n")
    print("      " + Diccionario[1] + " | " + Diccionario[2] + " | " + Diccionario[3])
    print("     ───|───|───")
    print("      " + Diccionario[4] + " | " + Diccionario[5] + " | " + Diccionario[6])
    print("     ───|───|───")
    print("      " + Diccionario[7] + " | " + Diccionario[8] + " | " + Diccionario[9])
    print("\n")

def fAsignarPosicion(position):
    if Diccionario[position] == ' ':
        return True 
    return False 

def fPosicionar(Caracter, position):
    if fAsignarPosicion(position):
        Diccionario[position] = Caracter 
        fTabla(Diccionario)
        if fDibujarEnTablero():
            print("Tablas, nadie ha ganado\n")
            exit()

        if fSacarGanador():
            if Caracter == Pc[0]:
                print(f"[{Pc[0]}] Computadora gana!!\n")
                exit()

            else:
                print(f"[{Jugador1[0]}] Has ganado!!\n")
                exit()
        return 
    else:
        print("Posicion ya ocupada!!")
        position = int(input(f"[{Jugador1[0]}] Ingrese una nueva posicion: del 1-9 -> "))
        fPosicionar(Caracter, position)
        return    

def fSacarGanador():
    if (Diccionario[1] == Diccionario[2] and Diccionario[1] == Diccionario[3] and Diccionario[1] != ' '):
        return True
    elif (Diccionario[4] == Diccionario[5] and Diccionario[4] == Diccionario[6] and Diccionario[4] != ' '):
        return True
    elif (Diccionario[7] == Diccionario[8] and Diccionario[7] == Diccionario[9] and Diccionario[7] != ' '):
        return True
    elif (Diccionario[1] == Diccionario[4] and Diccionario[1] == Diccionario[7] and Diccionario[1] != ' '):
        return True
    elif (Diccionario[2] == Diccionario[5] and Diccionario[2] == Diccionario[8] and Diccionario[2] != ' '):
        return True
    elif (Diccionario[3] == Diccionario[6] and Diccionario[3] == Diccionario[9] and Diccionario[3] != ' '):
        return True
    elif (Diccionario[1] == Diccionario[5] and Diccionario[1] == Diccionario[9] and Diccionario[1] != ' '):
        return True
    elif (Diccionario[7] == Diccionario[5] and Diccionario[7] == Diccionario[3] and Diccionario[7] != ' '):
        return True
    else:
        return False

def fGanador(Player):
    if (Diccionario[1] == Diccionario[2] and Diccionario[1] == Diccionario[3] and Diccionario[1] == Player):
        return True
    elif (Diccionario[4] == Diccionario[5] and Diccionario[4] == Diccionario[6] and Diccionario[4] == Player):
        return True
    elif (Diccionario[7] == Diccionario[8] and Diccionario[7] == Diccionario[9] and Diccionario[7] == Player):
        return True
    elif (Diccionario[1] == Diccionario[4] and Diccionario[1] == Diccionario[7] and Diccionario[1] == Player):
        return True
    elif (Diccionario[2] == Diccionario[5] and Diccionario[2] == Diccionario[8] and Diccionario[2] == Player):
        return True
    elif (Diccionario[3] == Diccionario[6] and Diccionario[3] == Diccionario[9] and Diccionario[3] == Player):
        return True
    elif (Diccionario[1] == Diccionario[5] and Diccionario[1] == Diccionario[9] and Diccionario[1] == Player):
        return True
    elif (Diccionario[7] == Diccionario[5] and Diccionario[7] == Diccionario[3] and Diccionario[7] == Player):
        return True
    else:
        return False

def fDibujarEnTablero():
    for key in Diccionario.keys():
        if Diccionario[key] == ' ':
            return False 
    return True 

def fMovimientos_Jugador():
    fTabla(Diccionario)
    position = int(input(f"[{Jugador1[0]}] Ingrese una nueva posicion: del 1-9 -> "))
    fPosicionar(Jugador1, position)
    os.system("cls")
    return 

def fMovimientos_Pc():
    bestScore = -800
    bestMove = 0
    Aleatorio = randrange(len(Diccionario))
    fTabla(Diccionario)
    for key in Diccionario.keys():
        if Diccionario[key] == ' ':
            Diccionario[key] = Pc
            score = fPonerFichas(Diccionario, False)
            Diccionario[key] = ' '
            if score > bestScore:
                bestScore = score 
                bestMove = key
    print(f"        \n[{Pc[0]}] Computadora esta eligiendo")
    time.sleep(5)
    fPosicionar(Pc, bestMove)
    return 

def fMovimientos_Pc2():
    bestScore = -800
    bestMove = 0
    Aleatorio = randrange(len(Diccionario))
    for key in Diccionario.keys():
        if Diccionario[key] == ' ':
            Diccionario[key] = Pc
            score = fPonerFichas(Diccionario, False)
            Diccionario[key] = ' '
            if score > bestScore:
                bestScore = score 
                bestMove = key
    print(f"        \n[{Pc[0]}] Computadora esta eligiendo")
    time.sleep(5)
    fPosicionar(Pc, bestMove)
    return 

def fMovimientos_Jugador2():
    position = int(input(f"\n[{Pc[0]}] Ingrese una nueva posicion: del 1-9 -> "))
    fPosicionar(Pc, position)
    return

def fFichaAleatoria(): # Libre para que el usuario que descargue este project lo haga, el 1 vs 1
    print("...")
    time.sleep(4)

def fPonerFichas(Diccionario, DibujarTablero):
    if fGanador(Pc):
        return 1 
    elif fGanador(Jugador1):
        return -1 
    elif fDibujarEnTablero():
        return 0
        
    if DibujarTablero:
        bestScore = -800 
        for key in Diccionario.keys():
            if Diccionario[key] == ' ':
                Diccionario[key] = Pc 
                score = fPonerFichas(Diccionario, False)
                Diccionario[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore 
    else:
        bestScore = 800 
        for key in Diccionario.keys():
            if Diccionario[key] == ' ':
                Diccionario[key] = Jugador1 
                score = fPonerFichas(Diccionario, True)
                Diccionario[key] = ' '
                if score < bestScore:
                    bestScore = score 
        return bestScore

while True:
    os.system("cls")
    Letras = ['A', 'B', 'C', 'D', 'E', 'F']
    Numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:
        os.system('cls')
        Color = []
        Combinacion1 = []
        Combinacion2 = []
        Almacen1 = ' '
        Almacen2 = ' '
        Aleatorio_L = randrange(len(Letras))
        Aleatorio_N = randrange(len(Numeros))

        Combinacion1 = Combinacion1 + [Aleatorio_L]
        Combinacion2 = Combinacion2 + [Aleatorio_N]

        for item in range(1):
            Almacen1 = Combinacion1[item]
            
        for item in range(1):
            Almacen2 = Combinacion2[item]

        os.system("cls")
        print("""
        ┌─────────────────────────────────────────────────────────┐
        │             Bienvenidos al juego Tic Tac Toe            │
        │_________________________________________________________│
        │                                                         │
        │    1 - Jugar                                            │
        │    2 - Reglas                                           │
        │    3 - Salir                                            │
        │                                                         │
        └─────────────────────────────────────────────────────────┘ 
        """)

        time.sleep(1)

        vOp = int(input("           ¿Cual eliges? "))

        if (vOp == 1):
            os.system("cls")
            print("""
            ┌─────────────────────────────────────────────────────────┐
            │             Bienvenidos al juego Tic Tac Toe            │
            │_________________________________________________________│
            │                                                         │
            │    1 - 1 vs pc                                          │
            │    2 - 1 vs 1                                           │
            │    3 - Activar modos                                    │
            │    4 - Salir                                            │
            │                                                         │
            └─────────────────────────────────────────────────────────┘ 
            """)
            vOp = int(input("           ¿Cual eliges? "))
            
            if vOp == 1:
                while True:
                    Simbolo = input("           Que desea: [X] o [O]? ")
                    if (Simbolo.upper() == 'X'):
                        Jugador1 = 'X'
                        Pc = 'O'
                        break
                        
                    elif (Simbolo.upper() == 'O'):
                        Jugador1 = 'O'
                        Pc = 'X'
                        break
                        
                    else:
                        print("         Introduzca una ficha valida!!")
                    
                while not fSacarGanador():
                    fTabla(Diccionario)
                    os.system(f"COLOR {Almacen1}{Almacen2}")
                    fMovimientos_Pc()
                    fMovimientos_Jugador()

            elif vOp == 2:
                while True:
                    Simbolo = input("           Que desea: [X] o [O]? ")
                    if (Simbolo.upper() == 'X'):
                        Jugador1 = 'X'
                        Pc = 'O'
                        break
                        
                    elif (Simbolo.upper() == 'O'):
                        Jugador1 = 'O'
                        Pc = 'X'
                        break
                        
                    else:
                        print("         Introduzca una ficha valida!!")
                    
                while not fSacarGanador():
                    fTabla(Diccionario)
                    os.system(f"COLOR {Almacen1}{Almacen2}")
                    fMovimientos_Jugador2()
                    fMovimientos_Jugador()

            elif vOp == 3:
                os.system("cls")
                print("""
                ┌─────────────────────────────────────────────────────────┐
                │             Bienvenidos al juego Tic Tac Toe            │
                │_________________________________________________________│
                │                                                         │
                │    1 - Easy                                             │
                │    2 - Medium                                           │
                │    3 - Hard                                             │
                │                                                         │
                └─────────────────────────────────────────────────────────┘ 
                """)

                vOp = int(input("           ¿Cual eliges? "))

                if (vOp == 1):
                    print("MODO EASY ACTIVADO")
                
                elif (vOp == 2):
                    print("MODO MEDIUM ACTIVADO")

                elif (vOp == 3):
                    print("MODO HARD ACTIVADO")

            elif vOp == 4:
                exit()
                
        elif (vOp == 2):
            print("""
                Reglas del game:
                ──────────────────────────────────────────────────────────────────────────────
                - El primero en generar una linea con su simbolo en cualquier direccion gana -             
                ──────────────────────────────────────────────────────────────────────────────
                """)
            os.system("pause")

        elif (vOp == 3):
            exit()