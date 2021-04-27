import random
from os import system, name
def telaInicial():
    print("_"* 150)
    print(" | SEJA BEM VINDO(A) AO JOGO DA VELHA DO FELLPS!")
    print(" | O JOGO CONSISTE EM UM TABULEIRO 3X3 ONDE AS JOGADAS SÃO ALTERNADAS ENTRE O USUÁRIO E O COMPUTADOR, VISANDO COMPLETAR UMA TRINCA")
    print(" | SEJA ELA EM HORIZONTAL, VERTICAL OU DIAGONAL, HAVENDO 8 POSSIBILIDADES DE OBTER VITÓRIA")
    print(" | O TABULEIRO ESTÁ DISTRIBUIDO DA SEGUINTE FORMA:")
    print(" | ")
    print(f" |  7 | 8 | 9")
    print(" | ---+---+---")
    print(f" |  4 | 5 | 6")
    print(" | ---+---+---")
    print(f" |  1 | 2 | 3")
    print(" | ")
    print(" | É CONSIDERADO VITÓRIA EM CASO DE:")
    print(" |      AO COMPLETAR AS LINHAS HORIZONTAIS 1, 2 E 3; 4, 5, E 6; 7, 8 E 9, OU")
    print(" |      AO COMPLETAR AS LINHAS VERTICAIS 1, 4 E 7; 2, 5 E 8; 3, 6 E 9, OU")
    print(" |      AO COMPLETAR AS DUAS DIAGONAIS 1, 5 E 9; 3, 5 E 7.")
    print(" |      CASO TODO O TABULEIRO SEJA PREENCHIDO E NENHUM JOGADOR COMPLETOU UMA TRINCA É CONSIDERADO EMPATE.")
    print(" | ")
    print(" | NO INICIO DO JOGO O USUÁRIO PODE ESCOLHER ENTRE 'X' OU 'O' PARA JOGAR, CONSEQUENTEMENTE O COMPUTADOR SERÁ A LETRA QUE O USUÁRIO NÃO ESCOLHEU.")
    print(" | APÓS ISSO, DE FORMA ALEATÓRIA O PROGRAMA DECIDE QUEM SERÁ O PRIMEIRO A JOGAR.")
    print("_"* 150)
    print("")
    print("")
    print("")
    print("")

    _ = input("---> Tecle Enter para Jogar.")
def auxiliar(Letra, tabuleiro):
    """
    Função auxiliar para jogada do computador, esta função compõe a estratégia e serve para verificar se o computador esta prestes a ganhar 
    e assim fazer a jogada correta, ou se o jogador está prestes a ganhar e assim o impedir. Recebe como parametro o simbolo a ser analizado e o tabuleiro com as jogadas.
    Retorna a posição que o computador irá jogar.
    """
    if tabuleiro[1] == Letra and tabuleiro[2] == Letra and tabuleiro[3] == " ":
        return 3
    elif tabuleiro[1] == Letra and tabuleiro[3] == Letra and tabuleiro[2] == " ":
        return 2
    elif tabuleiro[2] == Letra and tabuleiro[3] == Letra and tabuleiro[1] == " ":
        return 1
    elif tabuleiro[4] == Letra and tabuleiro[5] == Letra and tabuleiro[6] == " ":
        return 6
    elif tabuleiro[4] == Letra and tabuleiro[6] == Letra and tabuleiro[5] == " ":
        return 5
    elif tabuleiro[5] == Letra and tabuleiro[6] == Letra and tabuleiro[4] == " ":
        return 4
    elif tabuleiro[7] == Letra and tabuleiro[8] == Letra and tabuleiro[9] == " ":
        return 9
    elif tabuleiro[7] == Letra and tabuleiro[9] == Letra and tabuleiro[8] == " ":
        return 8
    elif tabuleiro[8] == Letra and tabuleiro[9] == Letra and tabuleiro[7] == " ":
        return 7
    elif tabuleiro[1] == Letra and tabuleiro[4] == Letra and tabuleiro[7] == " ":
        return 7
    elif tabuleiro[1] == Letra and tabuleiro[7] == Letra and tabuleiro[4] == " ":
        return 4
    elif tabuleiro[4] == Letra and tabuleiro[7] == Letra and tabuleiro[1] == " ":
        return 1
    elif tabuleiro[2] == Letra and tabuleiro[5] == Letra and tabuleiro[8] == " ":
        return 8
    elif tabuleiro[2] == " " and tabuleiro[5] == Letra and tabuleiro[8] == Letra:
        return 2
    elif tabuleiro[2] == Letra and tabuleiro[5] == " " and tabuleiro[8] == Letra:
        return 5

    elif tabuleiro[3] == Letra and tabuleiro[6] == Letra and tabuleiro[9] == " ":
        return 9
    elif tabuleiro[3] == Letra and tabuleiro[6] == " " and tabuleiro[9] == Letra:
        return 6
    elif tabuleiro[3] == " " and tabuleiro[6] == Letra and tabuleiro[9] == Letra:
        return 3


    elif tabuleiro[1] == Letra and tabuleiro[5] == Letra and tabuleiro[9] == " ":
        return 9
    elif tabuleiro[1] == Letra and tabuleiro[5] == " " and tabuleiro[9] == Letra:
        return 5
    elif tabuleiro[1] == " " and tabuleiro[5] == Letra and tabuleiro[9] == Letra:
        return 1


    elif tabuleiro[3] == Letra and tabuleiro[5] == Letra and tabuleiro[7] == " ":
        return 7
    elif tabuleiro[3] == Letra and tabuleiro[5] == " " and tabuleiro[7] == Letra:
        return 5
    elif tabuleiro[3] == " " and tabuleiro[5] == Letra and tabuleiro[7] == Letra:
        return 3
def auxiliar2(Letra, tabuleiro):
    """
    Função auxiliar para jogada do computador, esta função compõe a estratégia e é responsável por realizar uma das jogadas do computador. Recebe como parâmetro o Simbolo do computador
    e retorna a jogada que será realizada.
    """
    if Letra == "X":
        Letra2 = "O"
    else:
        Letra2 = "X"
    if tabuleiro[1] == Letra2 and tabuleiro[5] == Letra:
        if tabuleiro[3] == Letra:
            return 7
        elif tabuleiro[2] == Letra:
            return 8
        elif tabuleiro[4] == Letra:
            return 6
        elif tabuleiro[6] == Letra:
            return 4
        elif tabuleiro[7] == Letra:
            return 3
        elif tabuleiro[8] == Letra:
            return 2

        elif tabuleiro[9] == Letra:
            jogada = random.choice([3, 7])
            return jogada


    elif tabuleiro[3] == Letra and tabuleiro[5] == Letra2:
        if tabuleiro[1] == Letra2:
            return 9
        elif tabuleiro[2] == Letra2:
            return 8
        elif tabuleiro[4] == Letra2:
            return 6
        elif tabuleiro[6] == Letra2:
            return 4
        elif tabuleiro[8] == Letra2:
            return 2    
        elif tabuleiro[9] == Letra2:
            return 1

        elif tabuleiro[7] == Letra2:
            jogada = random.choice([9, 1])
            return jogada


    elif tabuleiro[7] == Letra and tabuleiro[5] == Letra2:
        if tabuleiro[1] == Letra2:
            return 9
        elif tabuleiro[2] == Letra2:
            return 8
        elif tabuleiro[4] == Letra2:
            return 6
        elif tabuleiro[6] == Letra2:
            return 4
        elif tabuleiro[8] == Letra2:
            return 2    
        elif tabuleiro[9] == Letra2:
            return 1

        elif tabuleiro[3] == Letra2:
            jogada = random.choice([9, 1])
            return jogada


    elif tabuleiro[9] == Letra and tabuleiro[5] == Letra2:
        if tabuleiro[3] == Letra2:
            return 7
        elif tabuleiro[2] == Letra2:
            return 8
        elif tabuleiro[4] == Letra2:
            return 6
        elif tabuleiro[6] == Letra2:
            return 4
        elif tabuleiro[7] == Letra2:
            return 3
        elif tabuleiro[8] == Letra2:
            return 2

        elif tabuleiro[1] == Letra2:
            jogada = random.choice([3, 7])
            return jogada
def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2020102152"
def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "FELIPE CAMILO SOARES" 
def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear')
def letra():
    """ 
    A função solicita ao usuário com qual simbolo ele deseja jogar. Retorna o simbolo escolhido pelo jogador e o simbolo remanescente para a máquina.
    """

    letraDoJogador = input("Deseja jogar com X ou O? ")
    if letraDoJogador in "Xx":
        return "X", "O"
    elif letraDoJogador in "Oo":
        return "O", "X"
    else:
        return letra()
def primeiroJogador():
    """
    A função escolhe de forma aleatória um numero entre [-1, 2), a função é chamada recursivamente até que retorne 1 ou -1.
    """
    x = random.randrange(-1, 2)
    if x == 0:
        return primeiroJogador()
    else:
        return x
def Tabuleiro(tab):
    """
    Pode receber como parâmetro a lista do tabuleiro com as posições vazias ou com as posições ja marcadas. Imprime na tela um tabuleiro no formato correto para o jogo da velha
    """
    print(f" {tab[7]} | {tab[8]} | {tab[9]}")
    print("---+---+---")
    print(f" {tab[4]} | {tab[5]} | {tab[6]}")
    print("---+---+---")
    print(f" {tab[1]} | {tab[2]} | {tab[3]}")
def jogadaDoUser(tab):
    """
    Recebe a lista do tabuleiro e pede ao usuário para realizar uma jogada. Verifica se a posição jogada está realmente vazia, caso esteja retorna a jogada,
    caso contrário a função é novamente chamada.
    """

    Tabuleiro(tab) #Imprime o tabuleiro com as jogadas atualizadas.
    x = int(input("onde deseja jogar? "))
    if x != 0:
        limpaTela()
        if tab[x] == " ":
            return x
        else:
            return jogadaDoUser(tab)
    else:
        return jogadaDoUser(tab)
def TesteCampeao(Letra, tabuleiro):
    """
    Recebe a Letra a ser verificada e o tabuleiro atualizado com as jogadas. Verifica se a letra recebida está em alguma das possibilidades de vitória, 
    que no caso são 8
    """
    if tabuleiro[1] == Letra and tabuleiro[2] == Letra and tabuleiro[3] == Letra:
        return True
    elif tabuleiro[4] == Letra and tabuleiro[5] == Letra and tabuleiro[6] == Letra:
        return True
    elif tabuleiro[7] == Letra and tabuleiro[8] == Letra and tabuleiro[9] == Letra:
        return True
    elif tabuleiro[1] == Letra and tabuleiro[4] == Letra and tabuleiro[7] == Letra:
        return True
    elif tabuleiro[2] == Letra and tabuleiro[5] == Letra and tabuleiro[8] == Letra:
        return True
    elif tabuleiro[3] == Letra and tabuleiro[6] == Letra and tabuleiro[9] == Letra:
        return True
    elif tabuleiro[1] == Letra and tabuleiro[5] == Letra and tabuleiro[9] == Letra:
        return True
    elif tabuleiro[3] == Letra and tabuleiro[5] == Letra and tabuleiro[7] == Letra:
        return True
    else:
        return False
def empate(tabuleiro):
    """
    Recebe o tabuleiro com as jogadas atualizadas e verifica se há alguma posição livre, ignorando a posilçao 0. Retorna False caso haja alguma posição livre e True caso o 
    tabuleiro estaja totalmente preenchido.
    """
    if " " in tabuleiro[1:]:
        return False # ainda tem posição livre
    else:
        return True #empate
def PosicoesLivres(a, i = 1, L = []):
    """
    Recebe a lista tab gerada inicialmente com as posições vazias, e como parametro opcional recebe uma lista L. Retorna uma Lista com as posições livres.
    """
    
    L = [i for i in range(1, len(a)) if a[i] == " "] #gera uma lista a partir do tabuleiro que foi passado como parâmetro.
    return L
def aleatorio(L):
    """
    Escolhe uma posição livre do tabuleiro L passado como parâmetro e returna a posição escolhida.
    """
    return random.randrange(1, len(L) + 1)
def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia:
    Explique aqui, de forma resumida, a sua estratégia usada para o computador vencer o jogador.
    Inicialmente há a possibilidade do computador ser o primeiro a jogar, ou o usuário o primeiro. Caso o computador seja o primeiro ele seleciona
    uma das 4 pontas (1, 3, 7, 9)
    Depois verifica a jogada do usuário e joga na posição 5, caso a posição 5 seja selecionada o computador joga na extremidade oposta ao primeiro movimento.
    Após isso o computador analisa se é possivel ganhar e realiza o movimento, caso contrário entra em modo de defesa, verificando se o usuário está prestes a ganhar
    e bloqueando a jogada do usuário. É assim até que o computador ganhe ou dê empate.

    Caso seja o segundo à jogar o computador verifica se a posição 5 está livre para ser jogada, pois a posição 5 ira diminuir as chances do usuário vencer, independente de onde tenha
    jogado.
    Logo após a jogada do usuário o programa entra em modo de defesa, verificando se há algum espaço onde o usuário possa ganhar. Caso o usuário não esteja prestes a vencer
    o programa ira realizar uma jogada na qual não implique vitória ao usuário (por exemplo: o usuário jogou 1 e 9, o computador jogou 5 e está prestes a jogar 3, neste caso
    o usuário pode jogar na posição 7 para impedir que o computador vença e isso gera duas possibilidades de vitória para o usuário em 4 e 8, impedindo assim que o computador ganhe.)
    Dai em diante o computador apenas bloqueia as jogadas do usuário.
    """
    rodada = 9 - len(PosicoesLivres(tabuleiro))
    if simboloComputador == "X":
        jogador = "O"
    else:
        jogador = "X"

        
    if rodada == 0:##########################################################################igual
        jogada = random.choice([1, 3, 7, 9])
        return jogada
    if rodada == 1:##########################################################################igual

        if tabuleiro[5] == " ":
            return 5
        else:
            jogada = random.choice([1, 3, 7, 9])
            return jogada
    if rodada == 2:##########################################################################igual
        if tabuleiro[5] == " ":
            return 5
        else:
            if tabuleiro[1] == simboloComputador:
                return 9
            elif tabuleiro[3] == simboloComputador:
                return 7
            elif tabuleiro[7] == simboloComputador:
                return 3
            elif tabuleiro[9] == simboloComputador:
                return 1
    if rodada == 3:##########################################################################igual
        aux2 = auxiliar2(simboloComputador, tabuleiro)
        if aux2 != None:
            return aux2
        else:
            if tabuleiro[5] == simboloComputador and tabuleiro[2] == jogador:
                if tabuleiro[3] == jogador:
                    return 1
                elif tabuleiro[1] == jogador:
                    return 3
                else:
                    if tabuleiro[4] == jogador:
                        return 1 
                    elif tabuleiro[9] == jogador:
                        return 4
                    elif tabuleiro[7] == jogador:
                        return 6
                    elif tabuleiro[8] == jogador:
                        jogada = random.choice([6, 4])
                        return jogada



            if tabuleiro[5] == simboloComputador and tabuleiro[1] == jogador:###
                if tabuleiro[3] == jogador:
                    return 2
                elif tabuleiro[2] == jogador:
                    return 3
                elif tabuleiro[4] == jogador:
                    return 7
                elif tabuleiro[7] == jogador:
                    return 4
                else:
                    if tabuleiro[9] == jogador:
                        jogada = random.choice([2, 4, 6, 8])
                        return jogada
                    elif tabuleiro[6] == jogador:
                        return 3
                    elif tabuleiro[8] == jogador:
                        return 7

            if tabuleiro[5] == simboloComputador and tabuleiro[3] == jogador:###
                if tabuleiro[1] == jogador:
                    return 2
                elif tabuleiro[4] == jogador:
                    return 7
                elif tabuleiro[6] == jogador:
                    return 9
                elif tabuleiro[9] == jogador:
                    return 6

                else:
                    if tabuleiro[7] == jogador:
                        jogada = random.choice([2, 4, 6, 8])
                        return jogada
                    elif tabuleiro[2] == jogador:
                        return 1
                    elif tabuleiro[8] == jogador:
                        return 4

            if tabuleiro[5] == simboloComputador and tabuleiro[4] == jogador:###
                if tabuleiro[7] == jogador:
                    return 1
                elif tabuleiro[1] == jogador:
                    return 7
                else:
                    if tabuleiro[9] == jogador:
                        return 7
                    elif tabuleiro[6] == jogador:
                        return 3
                    elif tabuleiro[3] == jogador:
                        return 1
                    elif tabuleiro[2] == jogador:
                        return 1 
                    elif tabuleiro[8] == jogador:
                        return 7

            if tabuleiro[5] == simboloComputador and tabuleiro[6] == jogador:###
                if tabuleiro[9] == jogador:
                    return 3
                elif tabuleiro[3] == jogador:
                    return 9
                else:
                    if tabuleiro[7] == jogador:
                        return 9
                    elif tabuleiro[1] == jogador:
                        return 3
                    elif tabuleiro[4] == jogador:
                        return 7
                    elif tabuleiro[2] == jogador:
                        return 3 
                    elif tabuleiro[8] == jogador:
                        return 9

            if tabuleiro[5] == simboloComputador and tabuleiro[7] == jogador:###
                if tabuleiro[1] == jogador:
                    return 4
                elif tabuleiro[4] == jogador:
                    return 1
                elif tabuleiro[8] == jogador:
                    return 9
                elif tabuleiro[9] == jogador:
                    return 8
                else:
                    if tabuleiro[2] == jogador:
                        return 3
                    elif tabuleiro[4] == jogador:
                        return 3
                    elif tabuleiro[6] == jogador:
                        return 3

            if tabuleiro[5] == simboloComputador and tabuleiro[8] == jogador:###
                if tabuleiro[9] == jogador:
                    return 7
                elif tabuleiro[7] == jogador:
                    return 9
                else:
                    if tabuleiro[3] == jogador:
                        return 9
                    elif tabuleiro[6] == jogador:
                        return 1
                    elif tabuleiro[4] == jogador:
                        return 3
                    elif tabuleiro[2] == jogador:
                        return 3 
                    elif tabuleiro[1] == jogador:
                        return 7


            if tabuleiro[5] == simboloComputador and tabuleiro[9] == jogador:###
                if tabuleiro[8] == jogador:
                    return 7
                elif tabuleiro[6] == jogador:
                    return 3
                elif tabuleiro[3] == jogador:
                    return 6
                elif tabuleiro[7] == jogador:
                    return 8
                else:
                    if tabuleiro[2] == jogador:
                        return 1
                    elif tabuleiro[4] == jogador:
                        return 1
                    elif tabuleiro[1] == jogador:
                        return 2
    if rodada == 4:##########################################################################igual
        aux = auxiliar(simboloComputador, tabuleiro)  
        if aux != None:
            return aux
        else:
            aux1 = auxiliar(jogador, tabuleiro)
            if aux1 != None:
                return aux1
            else:
                aux2 = auxiliar2(jogador, tabuleiro)
                if aux2 != None:
                    return aux2
                else:
                    if tabuleiro[5] == simboloComputador and tabuleiro[2] == jogador:
                        if tabuleiro[3] == jogador:
                            return 1
                        elif tabuleiro[1] == jogador:
                            return 3
                        else:
                            if tabuleiro[4] == jogador:
                                return 1 
                            elif tabuleiro[9] == jogador:
                                return 4
                            elif tabuleiro[7] == jogador:
                                return 6
                            elif tabuleiro[8] == jogador:
                                jogada = random.choice([6, 4])
                                return jogada



                    if tabuleiro[5] == simboloComputador and tabuleiro[1] == jogador:###
                        if tabuleiro[3] == jogador:
                            return 2
                        elif tabuleiro[2] == jogador:
                            return 3
                        elif tabuleiro[4] == jogador:
                            return 7
                        elif tabuleiro[7] == jogador:
                            return 4
                        else:
                            if tabuleiro[9] == jogador:
                                jogada = random.choice([2, 4, 6, 8])
                                return jogada
                            elif tabuleiro[6] == jogador:
                                return 3
                            elif tabuleiro[8] == jogador:
                                return 7

                    if tabuleiro[5] == simboloComputador and tabuleiro[3] == jogador:###
                        if tabuleiro[1] == jogador:
                            return 2
                        elif tabuleiro[4] == jogador:
                            return 7
                        elif tabuleiro[6] == jogador:
                            return 9
                        elif tabuleiro[9] == jogador:
                            return 6

                        else:
                            if tabuleiro[7] == jogador:
                                jogada = random.choice([2, 4, 6, 8])
                                return jogada
                            elif tabuleiro[2] == jogador:
                                return 1
                            elif tabuleiro[8] == jogador:
                                return 4

                    if tabuleiro[5] == simboloComputador and tabuleiro[4] == jogador:###
                        if tabuleiro[7] == jogador:
                            return 1
                        elif tabuleiro[1] == jogador:
                            return 7
                        else:
                            if tabuleiro[9] == jogador:
                                return 7
                            elif tabuleiro[6] == jogador:
                                return 3
                            elif tabuleiro[3] == jogador:
                                return 1
                            elif tabuleiro[2] == jogador:
                                return 1 
                            elif tabuleiro[8] == jogador:
                                return 7

                    if tabuleiro[5] == simboloComputador and tabuleiro[6] == jogador:###
                        if tabuleiro[9] == jogador:
                            return 3
                        elif tabuleiro[3] == jogador:
                            return 9
                        else:
                            if tabuleiro[7] == jogador:
                                return 9
                            elif tabuleiro[1] == jogador:
                                return 3
                            elif tabuleiro[4] == jogador:
                                return 7
                            elif tabuleiro[2] == jogador:
                                return 3 
                            elif tabuleiro[8] == jogador:
                                return 9

                    if tabuleiro[5] == simboloComputador and tabuleiro[7] == jogador:###
                        if tabuleiro[1] == jogador:
                            return 4
                        elif tabuleiro[4] == jogador:
                            return 1
                        elif tabuleiro[8] == jogador:
                            return 9
                        elif tabuleiro[9] == jogador:
                            return 8
                        else:
                            if tabuleiro[2] == jogador:
                                return 3
                            elif tabuleiro[4] == jogador:
                                return 3
                            elif tabuleiro[6] == jogador:
                                return 3

                    if tabuleiro[5] == simboloComputador and tabuleiro[8] == jogador:###
                        if tabuleiro[9] == jogador:
                            return 7
                        elif tabuleiro[7] == jogador:
                            return 9
                        else:
                            if tabuleiro[3] == jogador:
                                return 9
                            elif tabuleiro[6] == jogador:
                                return 1
                            elif tabuleiro[4] == jogador:
                                return 3
                            elif tabuleiro[2] == jogador:
                                return 3 
                            elif tabuleiro[1] == jogador:
                                return 7


                    if tabuleiro[5] == simboloComputador and tabuleiro[9] == jogador:###
                        if tabuleiro[8] == jogador:
                            return 7
                        elif tabuleiro[6] == jogador:
                            return 3
                        elif tabuleiro[3] == jogador:
                            return 6
                        elif tabuleiro[7] == jogador:
                            return 8
                        else:
                            if tabuleiro[2] == jogador:
                                return 1
                            elif tabuleiro[4] == jogador:
                                return 1
                            elif tabuleiro[1] == jogador:
                                return 2
    if rodada == 5:##########################################################################igual
        aux = auxiliar(simboloComputador, tabuleiro)  
        if aux != None:
            return aux
        else:
            aux1 = auxiliar(jogador, tabuleiro)
            if aux1 != None:
                return aux1
            else:
                aux2 = auxiliar2(jogador, tabuleiro)
                if aux2 != None:
                    return aux2
                else:
                    if tabuleiro[5] == simboloComputador and tabuleiro[2] == jogador:
                        if tabuleiro[3] == jogador:
                            return 1
                        elif tabuleiro[1] == jogador:
                            return 3
                        else:
                            if tabuleiro[4] == jogador:
                                return 1 
                            elif tabuleiro[9] == jogador:
                                return 4
                            elif tabuleiro[7] == jogador:
                                return 6
                            elif tabuleiro[8] == jogador:
                                jogada = random.choice([6, 4])
                                return jogada



                    if tabuleiro[5] == simboloComputador and tabuleiro[1] == jogador:###
                        if tabuleiro[3] == jogador:
                            return 2
                        elif tabuleiro[2] == jogador:
                            return 3
                        elif tabuleiro[4] == jogador:
                            return 7
                        elif tabuleiro[7] == jogador:
                            return 4
                        else:
                            if tabuleiro[9] == jogador:
                                jogada = random.choice([2, 4, 6, 8])
                                return jogada
                            elif tabuleiro[6] == jogador:
                                return 3
                            elif tabuleiro[8] == jogador:
                                return 7

                    if tabuleiro[5] == simboloComputador and tabuleiro[3] == jogador:###
                        if tabuleiro[1] == jogador:
                            return 2
                        elif tabuleiro[4] == jogador:
                            return 7
                        elif tabuleiro[6] == jogador:
                            return 9
                        elif tabuleiro[9] == jogador:
                            return 6

                        else:
                            if tabuleiro[7] == jogador:
                                jogada = random.choice([2, 4, 6, 8])
                                return jogada
                            elif tabuleiro[2] == jogador:
                                return 1
                            elif tabuleiro[8] == jogador:
                                return 4

                    if tabuleiro[5] == simboloComputador and tabuleiro[4] == jogador:###
                        if tabuleiro[7] == jogador:
                            return 1
                        elif tabuleiro[1] == jogador:
                            return 7
                        else:
                            if tabuleiro[9] == jogador:
                                return 7
                            elif tabuleiro[6] == jogador:
                                return 3
                            elif tabuleiro[3] == jogador:
                                return 1
                            elif tabuleiro[2] == jogador:
                                return 1 
                            elif tabuleiro[8] == jogador:
                                return 7

                    if tabuleiro[5] == simboloComputador and tabuleiro[6] == jogador:###
                        if tabuleiro[9] == jogador:
                            return 3
                        elif tabuleiro[3] == jogador:
                            return 9
                        else:
                            if tabuleiro[7] == jogador:
                                return 9
                            elif tabuleiro[1] == jogador:
                                return 3
                            elif tabuleiro[4] == jogador:
                                return 7
                            elif tabuleiro[2] == jogador:
                                return 3 
                            elif tabuleiro[8] == jogador:
                                return 9

                    if tabuleiro[5] == simboloComputador and tabuleiro[7] == jogador:###
                        if tabuleiro[1] == jogador:
                            return 4
                        elif tabuleiro[4] == jogador:
                            return 1
                        elif tabuleiro[8] == jogador:
                            return 9
                        elif tabuleiro[9] == jogador:
                            return 8
                        else:
                            if tabuleiro[2] == jogador:
                                return 3
                            elif tabuleiro[4] == jogador:
                                return 3
                            elif tabuleiro[6] == jogador:
                                return 3

                    if tabuleiro[5] == simboloComputador and tabuleiro[8] == jogador:###
                        if tabuleiro[9] == jogador:
                            return 7
                        elif tabuleiro[7] == jogador:
                            return 9
                        else:
                            if tabuleiro[3] == jogador:
                                return 9
                            elif tabuleiro[6] == jogador:
                                return 1
                            elif tabuleiro[4] == jogador:
                                return 3
                            elif tabuleiro[2] == jogador:
                                return 3 
                            elif tabuleiro[1] == jogador:
                                return 7


                    if tabuleiro[5] == simboloComputador and tabuleiro[9] == jogador:###
                        if tabuleiro[8] == jogador:
                            return 7
                        elif tabuleiro[6] == jogador:
                            return 3
                        elif tabuleiro[3] == jogador:
                            return 6
                        elif tabuleiro[7] == jogador:
                            return 8
                        else:
                            if tabuleiro[2] == jogador:
                                return 1
                            elif tabuleiro[4] == jogador:
                                return 1
                            elif tabuleiro[1] == jogador:
                                return 2
    if rodada == 6:##########################################################################igual
        aux = auxiliar(simboloComputador, tabuleiro)  
        if aux != None:
            return aux
        else:
            aux1 = auxiliar(jogador, tabuleiro)
            if aux1 != None:
                return aux1
            else:
                jogada = random.choice(PosicoesLivres(tabuleiro))
                return jogada
    if rodada == 7:##########################################################################igual
        aux = auxiliar(simboloComputador, tabuleiro)  
        if aux != None:
            return aux
        else:
            aux1 = auxiliar(jogador, tabuleiro)
            if aux1 != None:
                return aux1      
            else:
                jogada = random.choice(PosicoesLivres(tabuleiro))
                return jogada
    if rodada == 8:##########################################################################igual
            jogada = random.choice(PosicoesLivres(tabuleiro))
            return jogada
def jogadas(tab, quemJoga, LetraJogador, LetraComputador):
    """
    Recebe como parêmtro o tabuleiro, quem irá realizar a jogada e o simbolo de cada jogador. Chama as funções responsáveis por realizar as jogadas de cada jogador, verifica se 
    houve campeão ou empate e caso ainda tenha posições livres a função é chamada novamente, alternando entre os jogadores.
    """

    if PosicoesLivres(tab) != []: #verifica se ainda tem posição livre.
        if quemJoga == -1:
            jc = jogadaComputador(tab, LetraComputador) #chama a função jogada do computador.
            print(f"O Computador jogou {jc}")
            
            tab[jc] = LetraComputador #substitui o indice jc do tabuleiro pelo simbolo do computador.
             #print(PosicoesLivres(tab))
            campeao = TesteCampeao(LetraComputador, tab) #Chama a função que testa se o computador ganhou.
            if campeao:
                Tabuleiro(tab) #se o computador ganhou imprime o tabuleiro com a ultima jogada do computador e define uma mensagem de vitória.
                champ = "Que pena, o Computador ganhou!!"

        elif quemJoga == 1:
            ju = jogadaDoUser(tab) #chama a função da jogada do usuário.

            if ju != 0:
                tab[ju] = LetraJogador #substitui o indice jc do tabuleiro pelo simbolo do jogador.
                #print(PosicoesLivres(tab))
                
                campeao = TesteCampeao(LetraJogador, tab) #verifica se o jogador ganhou.
                if campeao: #se ganhou, define uma mensagem de vitória.
                    champ = "Parabéns, você ganhou!!!"
        if not campeao: #se não houver campeão verifica se tem empate.
            if empate(tab): #função do empate.
                Tabuleiro(tab)
                print("Velha!! O jogo terminou Empatado.") #houve empate
            else:
                jogadas(tab, quemJoga * (-1), LetraJogador, LetraComputador) 
                #Caso não houver empate, chama a função jogadas novamente, desta vez alternando 
                # entre os jogadores. (Multiplicando quemJoga por -1 o resultado sera sempre 1 ou -1.)

        else:
            print(champ) #imprimea mensagem de vitória.
def main():
    limpaTela()
    telaInicial() 
    limpaTela()
    tab = [" "]*10 #cria uma lista de tamanho 10, usando um quadrado para indicar espaços vazios.
    Tabuleiro(tab) #imprime a lista no formato de jogo da velha.
    LetraJogador, LetraComputador = letra() #atribui os valores retornados da função letra em duas variaveis.
    PrimeiroJogador = primeiroJogador() #Chama a função que define quem começa
    limpaTela()
    if PrimeiroJogador == 1:
        print("O primeiro a jogar é o Usuário.")
    else:
        print("O primeiro a jogar é o Computador.")
    jogadas(tab, PrimeiroJogador, LetraJogador, LetraComputador) #chama a função responsável por controlar o jogo.
    NewGame = input("Deseja jogar novamente? (S/N) ")
    if NewGame in "Ss":
        main()
    elif NewGame in "Nn":
        exit()
if __name__ == "__main__":
    main()