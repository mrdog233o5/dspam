from pynput import keyboard
from pyperclip import paste as getClipboard
from time import sleep

c = keyboard.Controller()
spam = False
msg = ""
count = 0

def toggle(key):
    global spam
    global msg
    if key != keyboard.Key.shift_l:
        return
    msg = getClipboard()
    spam = not spam


def send():
    global c

    c.press(keyboard.Key.cmd)
    c.press('v')
    c.release('v')
    c.release(keyboard.Key.cmd)

    c.tap(keyboard.Key.enter)
    sleep(0.1)

# Collect events until released
listener = keyboard.Listener(
    on_press=toggle)
listener.start()

while 1:
    if not spam:
        continue
    send()
    count += 1
    print(count)
