import random  

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palvra_secreta()
    letras_acertadas = inicializa_letras_acertadas('_', palavra_secreta)

    enforcou = False
    acertou = False 
    erros = 0

    desenha_forca(erros, letras_acertadas)    

    while (not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(7-erros))
    
        enforcou = erros == 7
        acertou =  "_" not in letras_acertadas 
        desenha_forca(erros, letras_acertadas)             

    imprime_resultado(acertou, palavra_secreta)

def imprime_mensagem_abertura():
    print("*********************************")
    print("*  Bem vindo ao jogo de Forca!  *")
    print("*********************************")  

def carrega_palvra_secreta():
    palavras = []

    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().upper()) 

    posicao = random.randrange(0, len(palavras))
    return palavras[posicao] 

def inicializa_letras_acertadas(caractere, palavra):
    return [caractere for letra in palavra]

def pede_chute():
    return str(input('\nInsira uma letra: ')).strip().upper()

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (letra == chute):
            letras_acertadas[index] = letra 
        index += 1

def imprime_resultado(acertou, palavra_secreta):
    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def imprime_mensagem_vencedor():
    print('')
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print('')

def imprime_mensagem_perdedor(palavra_secreta):
    print('')
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print('')   

def desenha_forca(erros, letras_acertadas):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")    

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    for s in letras_acertadas:
        print(s, end=' ')     

if (__name__ == "__main__"):
    jogar()