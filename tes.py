import os
import random
import threading
import tkinter as tk
import pyautogui
import winsound


def show_random_message():
    messages = [
        "Atenção!",
        "Cuidado!",
        "Perigo!",
        "Erro!",
        "Alerta!"
    ]
    message = random.choice(messages)

    window = tk.Toplevel(root)
    window.title(f"Alerta {message}")

    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    x = random.randint(0, width-200)
    y = random.randint(0, height-100)

    window.geometry("200x100+{}+{}".format(x, y))
    window.attributes("-topmost", True)

    label = tk.Label(window, text=message)
    label.pack(pady=20)

    button = tk.Button(window, text="Ok", command=window.destroy)
    button.pack(pady=10)

    # Move o mouse para uma posição aleatória na tela
    x = random.randint(0, width)
    y = random.randint(0, height)
    pyautogui.moveTo(x, y, duration=0.1)

    root.after(1, show_random_message)


def play_random_sound():
    while True:
        # Gera duas frequências aleatórias entre 1000 e 8000 Hz
        frequency1 = random.randint(1000, 8000)
        frequency2 = random.randint(1000, 8000)

        # Define a duração em milissegundos
        duration = 1000  # 1 segundo

        # Toca os sons
        winsound.Beep(frequency1, duration)
        winsound.Beep(frequency2, duration)




def start_thread():
    # Inicia as threads para as funções show_random_message e play_random_sound
    t1 = threading.Thread(target=show_random_message)
    t2 = threading.Thread(target=play_random_sound)

    t1.start()
    t2.start()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    start_thread()

    root.mainloop()
