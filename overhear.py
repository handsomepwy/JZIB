from pynput import keyboard
import time


def on_press(key):
    with open("record.txt", "a") as f:
        try:
            f.write(f"key {key.char} pressed at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")
        except AttributeError:
            f.write(f"key {key} pressed at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
