import pyperclip
import time
import random
import re

def is_already_shy(text):
    return "//blushes" in text or "//stutters" in text or re.search(r'\w-\w', text)

def shy_text_generator(text):
    words = text.split()
    shy_text = []
    for word in words:
        shy_word = ""
        for i, char in enumerate(word):
            if random.random() < 0.3 and i != 0:  # Add stutter with 30% chance
                shy_word += f"{char}-"
            shy_word += char
        if random.random() < 0.2:
            shy_text.append(shy_word + "~") 
        else:
            shy_text.append(shy_word)
        
    if random.random() < 0.3:
        return " ".join(shy_text) + " //blushes //stutters"
    else:
        return " ".join(shy_text)

def monitor_clipboard():
    last_text = ""
    print("Shy Text Generator is now watching your clipboard... (press Ctrl+C to stop)")
    
    try:
        while True:
            current_text = pyperclip.paste()
            if current_text != last_text and current_text.strip() and not is_already_shy(current_text):
                shy_version = shy_text_generator(current_text)
                pyperclip.copy(shy_version)
                last_text = shy_version
                print("✨ Shy version copied to clipboard!")
            else:
                last_text = current_text
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nStopped clipboard monitoring.")

if __name__ == "__main__":
    monitor_clipboard()
