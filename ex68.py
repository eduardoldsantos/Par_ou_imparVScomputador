from playsound import playsound
from random import randint
count = 0
while True:
    print('-=-' * 15)
    print('PAR OU IMPAR vs COMPUTADOR')
    print('-=-' * 15)
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    pi = str(input("Você quer par ou impar? ")) .upper()
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total da soma é {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else "DEU IMPAR")  # é possivel fazer estruturas de condição na mesma linha
    if pi == "PAR":
        if total % 2 == 0:
            print("Você venceu")
            print('=' * 15)
            count += 1
            playsound('tdcc.mp3')
        else:
            print("Você Perdeu")
            break
    elif pi == "IMPAR":
        if total % 2 == 1:
            print("Você venceu")
            count += 1
            playsound('tdcc.mp3')
        else:
            print("Você perdeu")
            break
    print("Vamos jogar novamente...")
print(f'GAME OVER! Você venceu {count}')
