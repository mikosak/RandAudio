import tkinter as tk
import time
import os
import random
from threading import Thread

try:
    import playsound
except ImportError:
    os.system("pip install playsound")
    import playsound

running = False

#### Commands ####

def validate(number):
    try:
        number = int(number)
        if number <= 0:
            raise ValueError
    except ValueError:
        instruction["text"] = "Please enter a whole number greater than zero."
        return False
    except:
        instruction["text"] = "Unknown error occured. Please try again."
        return False
    else:
        return number

def play_thread(min_secs, max_secs, path, current_dir):
    while running:
        rand_int = random.randint(min_secs, max_secs)
        rand_aud = path + "\\" + random.choice(current_dir)

        playsound.playsound(rand_aud)
        time.sleep(rand_int)


def start_playing():
    global running

    min_secs, max_secs = validate(lowlimit_entry.get()), validate(highlimit_entry.get())
    if min_secs == False or max_secs == False:
        return

    try:
        path = os.path.dirname(os.path.abspath(__file__))
        current_dir = list(filter(lambda x: x.endswith(".mp3"), os.listdir(path)))

        if len(current_dir) == 0:
            raise IndexError
    except IndexError:
        instruction["text"] = "Please ensure there are valid .mp3 files in the same folder as this script."
        return
    except:
        instruction["text"] = "Unknown error. Please check over your files and try again."
        return

    running = True
    play = Thread(target = play_thread, args = (min_secs, max_secs, path, current_dir), daemon = True)
    play.start()
    return

def stop_playing():
    global running
    running = False
    return

#### GUI ####

root = tk.Tk()
root.title("RandAudio Player")

instruction = tk.Label(root, text = "Please ensure files that you want played are in the same folder as this script. Support is only for .mp3 files.")
instruction.grid(row = 0, columnspan = 3)

lowlimit_label = tk.Label(root, text = "Minimum (secs): ")
lowlimit_label.grid(row = 1, column = 0)
lowlimit_entry = tk.Entry(root)
lowlimit_entry.grid(row = 1, column = 1)

highlimit_label = tk.Label(root, text = "Maximum (secs): ")
highlimit_label.grid(row = 2, column = 0)
highlimit_entry = tk.Entry(root)
highlimit_entry.grid(row = 2, column = 1)

start_btn = tk.Button(root, text = "Start player", command = start_playing)
start_btn.grid(row = 3)

end_btn = tk.Button(root, text = "Stop player", command = stop_playing)
end_btn.grid(row = 3, column = 2)

root.mainloop()