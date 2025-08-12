import tkinter as tk
import threading
import time
import random
import keyboard
import pyautogui
import sys
import os

# --------- PART 1: Fake Blue Screen of Death ---------
def fake_bsod():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(background='blue')
    root.title("Fatal Error")

    bsod_text = """
*** STOP: 0x0000007B (0xFFFFFFFFC0000034)

INACCESSIBLE_BOOT_DEVICE

A problem has been detected and Windows has been shut down to prevent damage to your computer.

If this is the first time you've seen this stop error screen,
restart your computer. If this screen appears again, follow
these steps:

Check to make sure any new hardware or software is properly installed.
If this is a new installation, ask your hardware or software manufacturer
for any Windows updates you might need.

If problems continue, disable or remove any newly installed hardware
or software. Disable BIOS memory options such as caching or shadowing.
If you need to use Safe Mode to remove or disable components, restart
your computer, press F8 to select Advanced Startup Options, and then
select Safe Mode.

Technical information:

*** STOP: 0x0000007B (0xFFFFFFFFC0000034)
    """

    label = tk.Label(root, text=bsod_text, fg='white', bg='blue', font=("Consolas", 18), justify="left")
    label.pack(expand=True)

    root.mainloop()

# --------- PART 2: Caps Lock Toggler ---------
def caps_lock_toggler():
    try:
        while True:
            time.sleep(random.uniform(3, 7))
            keyboard.press_and_release('caps lock')
    except:
        pass

# --------- PART 3: Mouse Jitter ---------
def mouse_jitter():
    try:
        while True:
            x, y = pyautogui.position()
            jitter_x = x + random.randint(-10, 10)
            jitter_y = y + random.randint(-10, 10)
            pyautogui.moveTo(jitter_x, jitter_y, duration=0.1)
            time.sleep(random.uniform(1, 3))
    except:
        pass

# --------- Run all pranks together in threads ---------
if __name__ == "__main__":
    print("Ultimate Hacker Prank Pack started!")
    print("To stop, focus terminal and press Ctrl+C")

    # Run fake BSOD in main thread (blocks)
    threading.Thread(target=caps_lock_toggler, daemon=True).start()
    threading.Thread(target=mouse_jitter, daemon=True).start()

    fake_bsod()
