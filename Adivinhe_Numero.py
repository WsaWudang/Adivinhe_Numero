import random

def jogar():
    Numero_Pc = random.randint(1, 100)
    limite_tentativas = 5
    tentativas = 0

    while tentativas < limite_tentativas:
        Numero_Usuario = int(input("Digite um número de 1 a 100 para tentar adivinhar o número que o Computador escolheu: "))
        if Numero_Usuario <= 0 or Numero_Usuario > 100:
            print("Você digitou um número inválido. Tente novamente!")
            continue
        tentativas += 1
        if Numero_Usuario == Numero_Pc:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s). O computador escolheu o número {Numero_Pc}.")
            break
        else:
            if Numero_Usuario < Numero_Pc:
                print(f"O número escolhido é maior que {Numero_Usuario}.")
            else:
                print(f"O número escolhido é menor que {Numero_Usuario}.")
            
    if tentativas == limite_tentativas:
        print(f"Você esgotou suas {limite_tentativas} tentativas. O número escolhido pelo computador era {Numero_Pc}.")

    jogar_novamente()

def jogar_novamente():
    novamente = input(f"Deseja jogar novamente? s/n " )
    if novamente.lower() == 's':
        jogar()
    else:
        print("Obrigado por jogar!\n")

jogar()