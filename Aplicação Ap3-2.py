import tkinter as tk
import random
import time
def poop():
    print(time.time()) # Undefined varr time
import pygame

# Inicialize o pygame
pygame.mixer.init()
pygame.mixer.music.load("song.mp3") 
pygame.mixer.music.set_volume(5)  # Ajuste o volume

# Lista de imagens 
images = {
    'aranha': 'A',
    'bola': 'B',
    'casa': 'C',
    'dado': 'D',
    'estrela': 'E',
    'faca': 'F',
    'gato': 'G',
    'helicoptero': 'H',
    'indio': 'I',
    'joaninha': 'J',
    'kombi': 'K',
    'lampada': 'L',
    'macaco': 'M',
    'navio': 'N',
    'oculos': 'O',
    'pato': 'P',
    'queijo': 'Q',
    'rato': 'R',
    'sapo': 'S',
    'telefone': 'T',
    'uva': 'U',
    'vaca': 'V',
    'whats': 'W',
    'xicara': 'X',
    'youtube': 'Y',
    'zebra': 'Z',    
}

def start_game():
    global score, current_image
    score = 0
    current_image = None
    play_background_music()
    next_image()

def play_background_music():
    pygame.mixer.music.play(-1)  # Reproduz a música

def next_image():
    global current_image
    if current_image is not None:
        canvas.delete(current_image)
    image_name, correct_letter = random.choice(list(images.items()))
    current_image = tk.PhotoImage(file=f"{image_name}.png")
    canvas.create_image(200, 200, image=current_image)
    label.config(text=f"Encontre a letra: {correct_letter}")
    start_timer()

def check_answer(letter):
    global score
    if letter == images[current_image]:
        score += 1
        next_image()

def start_timer():
    global timer
    timer = 10  # Tempo em segundos
    update_timer()

def update_timer():
    global timer
    if timer > 0:
        label_timer.config(text=f"Tempo restante: {timer} segundos")
        timer -= 1
        root.after(1000, update_timer)
    else:
        end_game(0)

def end_game():
    label_timer.config(text="Tempo esgotado!")
    canvas.delete(current_image)
    label.config(text=f"Jogo encerrado. Sua pontuação: {score}")
    pygame.mixer.music.stop()  # Pare a música quando o jogo terminar

root = tk.Tk()
root.title("ABC UnigranRioApp")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

label = tk.Label(root, text="", font=("Arial", 20))
label.pack()

buttons_frame = tk.Frame(root)
buttons_frame.pack()

for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    tk.Button(buttons_frame, text=letter, command=lambda l=letter: check_answer(l)).pack(side=tk.LEFT)

label_timer = tk.Label(root, text="", font=("Arial", 14))
label_timer.pack()

start_button = tk.Button(root, text="Iniciar Jogo", command=start_game)
start_button.pack()

start_game()
root.mainloop()
