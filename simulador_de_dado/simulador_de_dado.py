import random
import time
import turtle


def main():
    paint_anime()
    faz_pergunta()


def paint_anime():
    wn = turtle.Screen()
    cube = turtle.Turtle()
    cube.write('Data Simulator', move=False, align="left", font=("Arial", 12, "normal"))
    for i in range(4):
        cube.forward(200)
        cube.left(90)
        cube.forward(100)
    time.sleep(1)
    wn.bye()
    exit()

def faz_pergunta():
    question = input("Você gostaria de jogar o dado? (Pressione 'S' para CONFIRMAR ou qualquer tecla para SAIR): ")
    return valida_retorno(question)


def valida_retorno(resposta):
    while resposta.upper() == 'S':
        print('O número gerado foi: ', gera_numero())
        faz_pergunta()

    if resposta.upper() != 'S':
        print("Encerrando...")
        time.sleep(2)
        print("Até mais!!!")
        exit()


def gera_numero():
    return random.randrange(1, 7)


if __name__ == "__main__":
    main()
