import pygame
from sys import exit
import os

t = [""] * 9

def CheckWinner(t):
    # X même et les trois Y
    for x in range(3):
        if t[x * 3] == t[x * 3 + 1] == t[x * 3 + 2] != "":
            return t[x * 3]
    
    # Y meme et les trois X
    for y in range(3):
        if t[y] == t[y + 3] == t[y + 6] != "":
            return t[y]

    # X == Y pour les trois valeurs
    if t[0] == t[4] == t[8] != "":
        return t[0]
    
    # X + Y == 2 pour les trois valeurs de X
    if t[2] == t[4] == t[6] != "":
        return t[2]
    
    for i in range(9):
        if t[i] == "":
            return None  # Le jeu continue

    # Pas de Gagnant
    return "Draw"

def print_tableau(t):
    os.system("cls")
    for x in range(3):
        for y in range(3):
            if t[x * 3 + y] == "":
                print(f"  {x * 3 + y}  ", end="")
            else:
                print(f" {t[x * 3 + y]}  ", end="")
        print("\n")

tour = True
while True:
    # ENTRÉES (Input)
    coup = input(f"C'est au tour de { "❌" if tour else "⭕"}\nEntrez votre coup (0-8) : ")

    # ACTIONS (Update)
    try:
        index = int(coup)
        if 0 <= index <= 8 and t[index] == "":
            if tour:
                t[index] = "❌"
            else:
                t[index] = "⭕"
            tour = not tour
        else:
            print("Position invalide ou déjà occupée !")
            input("Appuyez sur Entrée...")
    except ValueError:
        print("Entrée invalide !")
        input("Appuyez sur Entrée...")

    # SORTIE (Affichage)
    print_tableau(t)
