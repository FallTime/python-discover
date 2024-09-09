def exibirtab(tabuleiro):
    print("\n")
    for i in range(1, 10):
        if tabuleiro[i] == 0:
            print("   ", end='')
        elif tabuleiro[i] == 1:
            print(" X ", end='')
        else:
            print(" O ", end='')

        if i % 3 == 0 and i < 9:
            print("\n-----------")
        else:
            if i != 9:
                print("|", end='')


def jogada(tabuleiro):
    global j1
    casa = int(input("\n\nInsira a posição:"))

    if casa < 1 or casa > 10:
        print("\nPosição invalida")
        return False

    ehdisponivel = tabuleiro[casa] == 0

    if ehdisponivel:
        if j1:
            tabuleiro[casa] = 1
            j1 = False
        else:
            tabuleiro[casa] = -1
            j1 = True
        return True
    else:
        print("\nCasa indisponível")
        return False

def estado(tabuleiro):
    # victory cases 123,147,159,528,546,537,987,963
    global jv
    
    if tabuleiro[1] + tabuleiro[2] + tabuleiro[3] == 3 or \
       tabuleiro[1] + tabuleiro[4] + tabuleiro[7] == 3 or \
       tabuleiro[1] + tabuleiro[5] + tabuleiro[9] == 3 or \
       tabuleiro[5] + tabuleiro[2] + tabuleiro[8] == 3 or \
       tabuleiro[5] + tabuleiro[4] + tabuleiro[6] == 3 or \
       tabuleiro[5] + tabuleiro[3] + tabuleiro[7] == 3 or \
       tabuleiro[9] + tabuleiro[8] + tabuleiro[7] == 3 or \
       tabuleiro[9] + tabuleiro[6] + tabuleiro[3] == 3:
        jv = 1
        return False
        
    elif tabuleiro[1] + tabuleiro[2] + tabuleiro[3] == -3 or \
         tabuleiro[1] + tabuleiro[4] + tabuleiro[7] == -3 or \
         tabuleiro[1] + tabuleiro[5] + tabuleiro[9] == -3 or \
         tabuleiro[5] + tabuleiro[2] + tabuleiro[8] == -3 or \
         tabuleiro[5] + tabuleiro[4] + tabuleiro[6] == -3 or \
         tabuleiro[5] + tabuleiro[3] + tabuleiro[7] == -3 or \
         tabuleiro[9] + tabuleiro[8] + tabuleiro[7] == -3 or \
         tabuleiro[9] + tabuleiro[6] + tabuleiro[3] == -3:
        jv = -1
        return False

    return True


j1 = True # 
jv = 0
zerado = [0 for i in range(10)]
tabuleiro = zerado.copy()

while estado(tabuleiro) and tabuleiro[0] < 9:
    exibirtab(tabuleiro)
    if jogada(tabuleiro):
        tabuleiro[0] += 1

exibirtab(tabuleiro)

print("\n\nVelha " if tabuleiro[0] == 9 else "\n\nX venceu" if jv == 1  else "\n\nO Venceu")
