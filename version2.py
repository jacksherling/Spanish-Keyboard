from pynput import keyboard
from pynput.keyboard import Key, Controller
#import pygame
#from pygame import *
import time

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
    'N': 'Ñ',
    '$': '€',
    'p': 'π',
    'P': 'π',
    '*': '°',
    's': '§',
    'S': '§',
    '-': '–',
    '_': '—',
    '+': '±',
    '0': 'θ',
    '.': '•',
    ':': '∷',
    ';': '∴',
    '=': '≅',
    '~': '≈',
    '<': '≤',
    '>': '≥',
    '^': '↑',
    '8': '∞',
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
        active = True
        lastkey = k
        t = 0
    else:
        active = False
        lastkey = False
        t = 0


def check_release(key):
    global active, keyboard_controller, lastkey, t
    try:
        k = key.char  # single-char keys
        if key.char in translate.values():
            return
    except:
        k = key.name  # other keys
        if key.name == "backspace":
            return
    if k == lastkey:
        if t >= 6 and active:
            active = False
            lastkey = False
            t = 0
            keyboard_controller.press(Key.backspace)
            keyboard_controller.release(Key.backspace)
            # type new key
            keyboard_controller.type(translate[k])


# key listeners
listener = keyboard.Listener(
    on_press=check, on_release=check_release, supress=True)
listener.start()

print("Welcome to Jack's Keyboard!\nHere are the key mappings:")
for x in translate.keys():
    print(x + " → " + translate[x])
print("Simply hold down one of your keys for a bit longer than usual, lift your finger up, and you're done! You should have a new character.")

# end program when user closes pygame
while running:
    t += 1
    time.sleep(0.05)
