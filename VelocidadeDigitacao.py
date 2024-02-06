import random
import time
import sys
from termcolor import colored
import msvcrt

def exibir_texto_com_destaque(texto_entrada, indice_atual, entrada_usuario):
    texto_exibicao = ""
    for i, caractere in enumerate(texto_entrada):
        if i < indice_atual:
            texto_exibicao += colored(caractere, 'grey')  # Cor original do texto em cinza claro
        elif i == indice_atual:
            if entrada_usuario and entrada_usuario[-1] == caractere:
                texto_exibicao += colored(caractere, 'white', 'on_red')  # Fundo vermelho
            else:
                texto_exibicao += colored(caractere, 'white', 'on_blue')  # Fundo azul
        else:
            texto_exibicao += colored(caractere, 'grey')  # Cor original do texto em cinza claro

    sys.stdout.write("\r" + texto_exibicao)
    sys.stdout.flush()

def contagem_regressiva():
    for i in range(3, 0, -1):
        sys.stdout.write(f"\r{i}")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r   \r")
    sys.stdout.flush()

def avaliar_desempenho(tempo_decorrido):
    if tempo_decorrido < 30:
        return "\033[0;32;40mÓtimo\033[0m"
    elif 30 <= tempo_decorrido <= 45:
        return "\033[0;34;40mBom\033[0m"  # bom de 30 a 45
    else:
        return "\033[0;31;40mRuim\033[0m"

def teste_velocidade():
    textos_entrada = [ "O ceu estava estrelado e a lua brilhava intensamente, iluminando a noite com sua luz prateada.",
                    "O passaro voou velozmente entre as arvores, exibindo suas asas coloridas em um espetaculo de liberdade.",
                    "O rio fluia calmamente, refletindo as montanhas e criando uma paisagem serena e encantadora.",
                    "As flores desabrochavam em um canteiro repleto de cores vibrantes, enchendo o ar com um perfume doce e envolvente."]

    texto_entrada = random.choice(textos_entrada)

    print("Preparando para o teste:")
    contagem_regressiva()

    print("\n" + texto_entrada + "\n")

    entrada_usuario = ""
    indice_atual = 0
    erros = 0  # Adiciona um contador de erros

    tempo_inicio = time.time()

    while indice_atual < len(texto_entrada):
        exibir_texto_com_destaque(texto_entrada, indice_atual, entrada_usuario)

        tecla = msvcrt.getch().decode("utf-8")
        tecla = tecla if len(tecla) == 1 else tecla.lower()

        if tecla == texto_entrada[indice_atual]:
            entrada_usuario += tecla
            indice_atual += 1
        else:
            erros += 1  # Incrementa o contador de erros ao digitar incorretamente

    tempo_fim = time.time()

    print("\n\nVocê digitou corretamente!")
    tempo_decorrido = tempo_fim - tempo_inicio
    print(f"Tempo decorrido: {tempo_decorrido:.2f} segundos")
    print(f"Número de erros: {erros}")  # Mostra o número total de erros
    desempenho = avaliar_desempenho(tempo_decorrido)
    print(f"Avaliação de desempenho: {desempenho}")

    print("\nTexto correto:")
    print(texto_entrada)

# Inicia o teste
teste_velocidade()
