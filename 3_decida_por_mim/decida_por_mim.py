import random
import time

def main():
    perguntas = dict({1: "Devo sair de casa hoje?",
                      2: "Devo adotar um cãozinho?",
                      3: "Será que vai chover hoje?",
                      4: "Devo pedir uma pizza ao invés de sushi?",
                      5: "Python é melhor que PHP?"})
    exibe_perguntas(perguntas)
    faz_pergunta(perguntas)


def exibe_perguntas(perguntas):
    todas_perguntas = ""
    pergunta_titulo = '\n' + str("<<<<< Decida por mim >>>>>").upper() + '\n'
    for pergunta in perguntas:
        todas_perguntas += str(pergunta) + '.' + perguntas[pergunta] + '\n'
    print(pergunta_titulo + todas_perguntas)
    return todas_perguntas


def faz_pergunta(perguntas):
    try:
        question = int(input("Selecione uma pergunta de 1 a 5 ou digite 0 para SAIR: "))
        return valida_retorno(question, perguntas)
    except:
        print('Valor informado deve ser um número inteiro de 1 a 5!')
        faz_pergunta(perguntas)


def valida_retorno(question, perguntas):
    if question == 0:
        print("Encerrando...")
        time.sleep(2)
        print("Até mais!!!")
    elif question not in range(1, 6):
        print('Valor informado é maior que 5! Valor deve ser um número inteiro de 1 a 5!')
        faz_pergunta(perguntas)
    else:
        respostas = ["Sim!",
                     "Não!",
                     "Talvez, quem sabe!",
                     "Dificil responder essa hein! Não sei te dizer!",
                     "Pense melhor sobre isso, me pergunte mais tarde!"]
        pergunta_selecionada = "Você perguntou: " + perguntas[question] + '\n' + "Resposta: " + random.choice(respostas)
        return print(pergunta_selecionada)


if __name__ == "__main__":
    main()
