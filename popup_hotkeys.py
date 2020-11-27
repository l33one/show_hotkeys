from pynput import keyboard
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import time

EXIT = {keyboard.Key.ctrl, keyboard.Key.esc}
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='a')}, # Shift + a
    {keyboard.Key.shift, keyboard.KeyCode(char='A')}, # Shift + A
    {keyboard.Key.ctrl, keyboard.KeyCode(char='S')}, # Ctrl + S
    {keyboard.Key.ctrl, keyboard.KeyCode(char='s')}, # Ctrl + s
    {keyboard.Key.ctrl, keyboard.KeyCode(char='c')}, # Ctrl + c
    {keyboard.Key.ctrl, keyboard.KeyCode(char='C')}, # Ctrl + C
    {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.KeyCode(char='c')}, # Ctrl + Shift + c
    {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.KeyCode(char='C')}, # Ctrl + Shift + C
    {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.KeyCode(char='v')}, # Ctrl + Shift + v
    {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.KeyCode(char='V')}, # Ctrl + Shift + V
    {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode(char='C')}, # Ctrl + C
    {keyboard.Key.alt, keyboard.Key.tab}, # Alt + Tab
    {keyboard.Key.ctrl, keyboard.KeyCode(char='f')}, # Ctrl + f
    {keyboard.Key.ctrl, keyboard.KeyCode(char='F')}, # Ctrl + F
    {keyboard.Key.ctrl, keyboard.Key.esc}, # ctrl + esc
    {keyboard.Key.ctrl, keyboard.KeyCode(char='z')}, # ctrl + z
    {keyboard.Key.ctrl, keyboard.KeyCode(char='Z')}, # ctrl + Z
    {keyboard.Key.ctrl, keyboard.KeyCode(char='W')}, # ctrl + W
    {keyboard.Key.ctrl, keyboard.KeyCode(char='w')}, # ctrl + pgdw
    {keyboard.Key.ctrl, keyboard.KeyCode(char='w')}, # ctrl + pgup
    {keyboard.Key.shift, keyboard.Key.insert, keyboard.Key.ctrl} # Shift + Insert + Ctrl
]

current = set()

def show(text):
    hot_key = []
    for key in list(text):
        if str(key).startswith('Key'):
            hot_key.append(str(key).replace('Key.',''))
        else:
            hot_key.append(str(key).replace("'",''))
    hot_key.sort(key=len, reverse=True)
    joined_keys = " + ".join(hot_key)
    
    sg.SetOptions(element_padding=(0, 0))
    sg.popup(joined_keys,auto_close=True,auto_close_duration=1, 
    no_titlebar=True, button_type=sg.POPUP_BUTTONS_NO_BUTTONS,
    font=('serif',24),keep_on_top=True)

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute(current)

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

def execute(key):
    if key.difference(EXIT) == set():
        exit()
    show(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()