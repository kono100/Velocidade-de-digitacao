import random
import time
import sys
from termcolor import colored
import msvcrt

def display_text_with_highlight(input_text, current_index, user_input):
    display_text = ""
    for i, char in enumerate(input_text):
        if i < current_index:
            display_text += colored(char, 'grey')  # Original text color in light grey
        elif i == current_index:
            if user_input and user_input[-1] == char:
                display_text += colored(char, 'white', 'on_red')  # Background color red
            else:
                display_text += colored(char, 'white', 'on_blue')  # Background color blue
        else:
            display_text += colored(char, 'grey')  # Original text color in light grey

    sys.stdout.write("\r" + display_text)
    sys.stdout.flush()

def countdown():
    for i in range(3, 0, -1):
        sys.stdout.write(f"\r{i}")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r   \r")
    sys.stdout.flush()

def evaluate_performance(time_taken):
    if time_taken < 30:
        return "Ótimo"
    elif 40 <= time_taken <= 45:
        return "Bom"
    else:
        return "Ruim"

def test_speed():
    input_texts = [ "O ceu estava estrelado e a lua brilhava intensamente, iluminando a noite com sua luz prateada.",
                    "O passaro voou velozmente entre as arvores, exibindo suas asas coloridas em um espetaculo de liberdade.",
                    "O rio fluia calmamente, refletindo as montanhas e criando uma paisagem serena e encantadora.",
                    "As flores desabrochavam em um canteiro repleto de cores vibrantes, enchendo o ar com um perfume doce e envolvente."]

    input_text = random.choice(input_texts)

    print("Preparar-se para o teste:")
    countdown()

    print("\n" + input_text + "\n")

    user_input = ""
    current_index = 0
    erros = 0  # Adiciona um contador de erros

    start_time = time.time()

    while current_index < len(input_text):
        display_text_with_highlight(input_text, current_index, user_input)

        key = msvcrt.getch().decode("utf-8")
        key = key if len(key) == 1 else key.lower()

        if key == input_text[current_index]:
            user_input += key
            current_index += 1
        else:
            erros += 1  # Incrementa o contador de erros ao digitar incorretamente

    end_time = time.time()

    print("\n\nVocê digitou corretamente!")
    time_taken = end_time - start_time
    print(f"Tempo levado: {time_taken:.2f} segundos")
    print(f"Número de erros: {erros}")  # Mostra o número total de erros
    performance = evaluate_performance(time_taken)
    print(f"Avaliação de desempenho: {performance}")

    print("\nTexto correto:")
    print(input_text)

# Inicia o teste
test_speed()
