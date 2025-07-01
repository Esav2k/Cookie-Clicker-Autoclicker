import os
import pyautogui
import keyboard
import threading
import time
import tkinter as tk
from tkinter import PhotoImage

coordinates = None
clicking = False

def update_coordinates():
    global coordinates
    while True:
        if keyboard.is_pressed('F1'):
            coordinates = pyautogui.position()
            print(f"Position gesetzt: {coordinates}")
           
            while keyboard.is_pressed('F1'):
                time.sleep(0.1)
        time.sleep(0.1)

def click_loop():
    global clicking
    while True:
        if keyboard.is_pressed('q') and coordinates and not clicking:
            clicking = True
            print("Klickschleife gestartet")
            while clicking:
                pyautogui.click(coordinates)
                time.sleep(0.05)  
                if keyboard.is_pressed('w'):
                    clicking = False
                    print("Klickschleife gestoppt")
                    while keyboard.is_pressed('w'):
                        time.sleep(0.1)
        time.sleep(0.1)

def start_gui():
    def update_labels():
        coord_text = f"Position: {coordinates}" if coordinates else "Position: none"
        status_text = "Status: Klickend" if clicking else "Status: Stopp"
        label_coords.config(text=coord_text)
        label_status.config(text=status_text)
        window.after(500, update_labels)

    window = tk.Tk()
    window.title("Autoclicker")
    window.geometry("400x250")
    window.resizable(False, False)

    window.attributes("-topmost", True)

    icon_path = os.path.join(os.path.dirname(__file__), 'logo.png')
    if os.path.exists(icon_path):
        icon = PhotoImage(file=icon_path)
        window.iconphoto(True, icon)

    tk.Label(window, text="Autoclicker", font=("Arial", 24)).pack(pady=10)

    label_coords = tk.Label(window, text="Position: none", font=("Arial", 14))
    label_coords.pack(pady=10)

    label_status = tk.Label(window, text="Status: Stopp", font=("Arial", 14))
    label_status.pack(pady=10)

    tk.Label(window, text="Steuerung:", font=("Arial", 14, "underline")).pack(pady=5)
    tk.Label(window, text="F1: Position setzen\nq: Klick starten\nw: Klick stoppen", font=("Arial", 12)).pack()

    window.after(500, update_labels)
    window.mainloop()

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    threading.Thread(target=update_coordinates, daemon=True).start()
    threading.Thread(target=click_loop, daemon=True).start()
    start_gui()
