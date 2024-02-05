import time
import sys
from termcolor import colored
import msvcrt



def display_text_with_highlight(input_text, current_index, user_input):
    display_text = ""
    for i, char in enumerate(input_text):
        if i < current_index:
            display_text += char
        elif i == current_index:
            if user_input and user_input[-1] == char:
                display_text += colored(char, 'green')
            else:
                display_text += colored(char, 'white', 'on_red')  # Background color red for incorrect input
        else:
            display_text += ' '

    sys.stdout.write("\r" + display_text)
    sys.stdout.flush()

def test_speed():
    input_text = "Lorem i"
    print(input_text)
    print()

    user_input = ""
    current_index = 0

    start_time = time.time()

    while current_index < len(input_text):
        display_text_with_highlight(input_text, current_index, user_input)

        # Captura o próximo caractere sem precisar pressionar Enter usando a biblioteca msvcrt
        key = msvcrt.getch().decode("utf-8")
        key = key if len(key) == 1 else key.lower()

        if key == input_text[current_index]:
            user_input += key
            current_index += 1
        else:
            user_input += colored(key, 'white', 'on_red')  # Background color red for incorrect input
            display_text_with_highlight(input_text, current_index, user_input)
            time.sleep(0.5)  # Aguarda 0.5 segundos para destacar o caractere incorreto antes de reescrever

            # Limpa a linha e redefine o texto corretamente digitado
            sys.stdout.write("\r" + ' ' * len(input_text))
            sys.stdout.flush()
            user_input = ""
            current_index = 0

    end_time = time.time()

    print("\n\nVocê digitou corretamente!")
    time_taken = end_time - start_time
    print(f"Tempo levado: {time_taken:.2f} segundos")
    print("\nTexto correto:")
    print(input_text)

# Inicia o teste
test_speed()
