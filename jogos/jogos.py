import forca
import adivinhacao

def esolha():
    print("*********************************")
    print("*      Escolha o seu Jogo       *")
    print("*********************************") 

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo?\n"))

    if (jogo == 1):
        print("jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("jogando Adivinhação")
        adivinhacao.jogar()

    novo = input("Deseja jogar outro jogo? (S) Sim, (N) Não: ")
    if (novo == "S"):
        esolha()

if (__name__ == "__main__"):
    esolha()