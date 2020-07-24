import random
import time
import turtle


def main():
    numero_oculto = gera_numero()
    paint_anime()
    faz_pergunta(numero_oculto)


def paint_anime():
    wn = turtle.Screen()
    cube = turtle.Turtle()
    cube.write('Chute o Número', move=False, align="left", font=("Arial", 12, "normal"))
    for i in range(4):
        cube.forward(200)
        cube.left(90)
        cube.forward(100)
    time.sleep(1)
    wn.bye()


def faz_pergunta(numero_oculto):
    try:
        question = int(input("Chute um número inteiro de 1 a 10 ou digite 0 para SAIR: "))
        return valida_retorno(question, numero_oculto)
    except:
        print('Valor informado deve ser um número inteiro!')
        faz_pergunta(numero_oculto)


def valida_retorno(question, numero_oculto):
    if question == 0:
        print("Encerrando...")
        time.sleep(2)
        print("Até mais!!!")
    else:
        if question > numero_oculto:
            print("O número que voce escolheu é MAIOR que o número secreto.")
            faz_pergunta(numero_oculto)
        elif question < numero_oculto:
            print("O número que voce escolheu é MENOR que o número secreto.")
            faz_pergunta(numero_oculto)
        elif numero_oculto == question:
            print(f"Parabéns você acertou o número secreto {numero_oculto}.")


def gera_numero():
    return random.randrange(1, 11)


if __name__ == "__main__":
    main()
