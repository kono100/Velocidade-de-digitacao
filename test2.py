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
                # Highlight correct character in blue
                display_text += colored(char, 'white', 'on_blue')
            else:
                # Highlight incorrect character in red
                display_text += colored(char, 'white', 'on_red')
        else:
            display_text += colored(char, 'grey')  # Original text color in light grey

    # Verifica se a palavra completa está incorreta
    if user_input and input_text[:current_index + 1] != user_input:
        display_text = colored(display_text, 'white', 'on_red')

    sys.stdout.write("\r" + display_text)
    sys.stdout.flush()

def countdown():
    for i in range(3, 0, -1):
        sys.stdout.write(f"\r{i}")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r   \r")
    sys.stdout.flush()

def test_speed():
    input_texts = ["Lorem 1", "Lorem 2", "Lorem 3", "Lorem 4"]
    input_text = random.choice(input_texts)

    print("Preparar-se para o teste:")
    countdown()

    print("\n" + input_text + "\n")

    user_input = ""
    current_index = 0

    start_time = time.time()

    while current_index < len(input_text):
        display_text_with_highlight(input_text, current_index, user_input)

        key = msvcrt.getch().decode("utf-8")
        key = key if len(key) == 1 else key.lower()

        if key == input_text[current_index]:
            user_input += key
            current_index += 1
        else:
            # Corrige a entrada do usuário removendo o caractere incorreto
            user_input = user_input[:-1]

    end_time = time.time()

    print("\n\nVocê digitou corretamente!")
    time_taken = end_time - start_time
    print(f"Tempo levado: {time_taken:.2f} segundos")
    print("\nTexto correto:")
    print(input_text)

# Inicia o teste
test_speed()
