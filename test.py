import time
from termcolor import colored

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

    print(display_text)

def test_speed():
    input_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    print(input_text)
    print()

    user_input = ""
    current_index = 0

    start_time = time.time()

    while current_index < len(input_text):
        display_text_with_highlight(input_text, current_index, user_input)
        key = input("Pressione a tecla correta: ")

        if key == input_text[current_index]:
            user_input += key
            current_index += 1
        else:
            user_input += colored(key, 'white', 'on_red')  # Background color red for incorrect input

    end_time = time.time()

    print("\nVocê digitou corretamente!")
    time_taken = end_time - start_time
    print(f"Tempo levado: {time_taken:.2f} segundos")
    print("\nTexto correto:")
    print(input_text)

# Inicia o teste
test_speed()
