#!/usr/bin/env python3
import sys # <-- o sys possui função para fechar o programa
import subprocess # <-- permite chamar programas externos
from modules.osint import menu_osint
from modules.rede import menu_rede
from modules.web import menu_web
from modules.brute import menu_brute
from modules.forense import menu_forense
from modules.wordlists import menu_wordlists


FMOUSEART = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠄⠄⢄⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠁⠅⠁⠅⠁⠅⠙⢕⢝⢥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⢕⢕⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⢕⢕⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠅⠁⠅⠁⠅⢅⢅⢅⢅⠅⠅⠁⠅⠙⠅⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠅⠁⢅⣥⣷⣧⢕⠝⣵⣿⣿⣇⢅⠁⠅⠁⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠁⠅⢁⣝⢿⣿⠟⣽⠕⠽⢿⣿⢟⢕⠁⠅⠁⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠅⠁⠅⢹⣿⣷⣷⢽⣿⠗⢕⢕⢕⢕⢕⢕⠅⠁⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠅⠁⠅⢽⣿⣿⣿⣿⣿⡗⢕⢕⢕⢕⢕⠕⠅⠁⠅⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠅⢹⣿⣿⣿⣿⣿⣿⢕⢕⢕⢕⢕⢕⠅⠁⠅⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠁⠅⠙⣿⣿⣿⣿⣿⣿⣗⢕⢕⢕⢕⠝⠅⠁⢅⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠁⠅⠁⠅⠁⢽⣿⣿⣿⣿⣿⣿⣝⢕⢕⢕⠅⠅⠁⢽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠄⠀⠅⠁⠅⠁⠅⠁⠅⠁⠝⣿⣿⣿⣿⣿⣿⣿⣷⠕⢕⠁⠅⠁⠕⢕⢕⠕⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠄⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⢹⣿⣿⣿⣿⣿⢝⢝⢕⠅⠁⠅⠁⠅⠁⠕⠅⠅⠉⠕⢅⠄⠀⠀
⠀⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⢿⣿⣿⣿⣿⠕⢕⠕⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠉⠕⢅⠀
⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠝⢿⣿⣿⣿⢕⢕⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠉⢅
⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⢹⣿⣿⣿⢕⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅
⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⢿⣿⣗⢝⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅
⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠽⣿⣅⠕⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅
⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⢿⣅⠅⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠄⠁⠅
⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠙⣿⠅⠅⠁⠅⠁⠅⠁⠅⠁⠄⠁⠅⠁⠅⠁⠅⠁⠅
⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠝⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅⠁⠅

"""

def limpar_tela(): # <-- cria função de limpar a tela
    subprocess.run(["clear"], check= True) # <-- se o clear der certo retorna 0 se nao retorna 1 ou seja:
    #o check e para ver se retornou 0 se sim, o programa continua

def menu_principal(): # <-- Cria função do menu principal
    while True:
        limpar_tela()
        print(FMOUSEART)
        print("=========================================")
        print("            FMOUSE TOOLKIT              ")
        print("=========================================")
        print("1 - Módulo de OSINT")
        print("2 - Módulo de Rede e Sniffing")
        print("3 - Módulo Web")
        print("4 - Módulo Senhas e Força Bruta")
        print("5 - Forense e Recuperação")
        print("6 - Wordlists")
        print("0 - Sair")
        print("=========================================")

        escolha = input("\n Escolha uma categoria \n")

        if escolha == "1":
            menu_osint()

        elif escolha == "2":
            menu_rede()

        elif escolha == "3":
            menu_web()

        elif escolha == "4":
            menu_brute()

        elif escolha == "5":
            menu_forense()

        elif escolha == "6":
            menu_wordlists()

        elif escolha == "0":
            print("Saindo do FMOUSE...")
            sys.exit(0)
        else:
            print("Opção inválida!")
            input("Pressione enter para continuar")

if __name__ == "__main__": # <-- se o __name__ (nome do app) for igual __main__ (codigo original), rode o menu principal
    menu_principal()