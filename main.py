from pynput import keyboard
from pynput.keyboard import Key, Controller
import pygame
from pygame import *
import time

# initialize pygame
pygame.init()

# screen creation
screen = pygame.display.set_mode( (200, 160) )

# set icon and caption
pygame.display.set_caption("Spanish Keyboard")

# variable initializaition
running = True

keyboard_controller = Controller()

active = False

lastkey = ''
t = 0

translate = {
    'a': 'á',
    'e': 'é',
    'i': 'í',
    'o': 'ó',
    'u': 'ú',
    'n': 'ñ',
    '?': '¿',
    '!': '¡',
    'A': 'Á',
    'E': 'É',
    'I': 'Í',
    'O': 'Ó',
    'U': 'Ú',
    'N': 'Ñ'
}

# checks if key is tapped and should be translated
def check(key):
    global active, keyboard_controller, lastkey, t
    try:
        k = key.char  # single-char keys
        if key.char in translate.values():
            return
    except:
        k = key.name  # other keys
        if key.name == "backspace":
            return
    if k in translate.keys():
        if lastkey == k and t < 2:
            # delate previous two keys
            keyboard_controller.press(Key.backspace)
            keyboard_controller.release(Key.backspace)
            keyboard_controller.press(Key.backspace)
            keyboard_controller.release(Key.backspace)
            # type new key
            keyboard_controller.type(translate[k])
            lastkey = ''
            t = 0
            return
    lastkey = k
    t = 0

# key listeners
listener = keyboard.Listener(on_press=check, supress=True)
listener.start()

# pygame visuals

# on screen directions
directions = "Welcome to Spanish Keyboard. Simply type the character you wish to change two times quickly on your keyboard. This was made by Jack Sherling."

# splits long string into lines for pygames
def getTextImages (str, lines):
    words = str.split(' ')
    font = pygame.font.SysFont('calibri', 20)
    switchline = len(words) // lines
    arr = []
    cur = 0
    curLine = ""
    for xi, x in enumerate(words):
        curLine += x + " "
        cur += 1
        if cur == switchline:
            cur = 0
            arr.append(font.render(curLine, True, (0, 0, 0)))
            curLine = ""
    return arr

text = getTextImages(directions, 7)

# make screen white, add text
screen.fill( (255, 255, 255) ) 
for x in range(len(text)):
    screen.blit(text[x], (5, x * 20))
pygame.display.update()

# end program when user closes pygame
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # timing for key presses
    t += 1
    time.sleep(0.1)
