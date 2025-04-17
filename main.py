import random
import tkinter as tk
from tkinter import messagebox

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

def generate_shy_text():
    input_text = input_field.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Warning", "Please enter some text!")
        return
    output_text = shy_text_generator(input_text)
    output_field.delete("1.0", tk.END)
    output_field.insert("1.0", output_text)

def copy_to_clipboard():
    output_text = output_field.get("1.0", tk.END).strip()
    if output_text:
        root.clipboard_clear()
        root.clipboard_append(output_text)
        root.update()
        messagebox.showinfo("Copied", "Output text copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No output text to copy!")

# Create the main window
root = tk.Tk()
root.title("Shy Text Generator")

# Input field
tk.Label(root, text="Input Text:").pack(pady=5)
input_field = tk.Text(root, height=2, width=50)
input_field.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Shy Text", command=generate_shy_text)
generate_button.pack(pady=5)

# Output field
tk.Label(root, text="Output Text:").pack(pady=5)
output_field = tk.Text(root, height=2, width=50)
output_field.pack(pady=5)

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Run the application
root.mainloop()
