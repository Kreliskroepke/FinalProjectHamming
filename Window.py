import tkinter as tk
from encoder import *
from decoder import *
from random import *

# --- External functions ---
def encode(text):
    return text[::-1]

def decode(text):
    return text[::-1]


def run_encode():
    """This takes a string, and returns the encoded message in the window"""
    user_input = entry.get()
    if not user_input.strip():
        output_label.config(text="Please fill in a message.")
        return
    result = encode(user_input)
    output_label.config(text=f"Encoded result:\n{result}")

def run_decode():
    """This takes a string, and returns the decoded message in the window"""
    user_input = entry.get()
    if not user_input.strip():
        output_label.config(text="Please fill in a message.")
        return
    result = decode(user_input)
    output_label.config(text=f"Decoded result:\n{result}")


#Create popup window
root = tk.Tk()
root.title("Hamming Code")
root.geometry("600x450")

#Text at top
title_label = tk.Label(root, text="Welcome to our Hamming en-/decoder!", font=("Arial", 11))
title_label.pack(pady=10)
expl_label = tk.Label(root, text="Give your message, and click a button.", font=("Arial", 11))
expl_label.pack(pady=0)

#Input field
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

#Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

encode_button = tk.Button(button_frame, text="Encode", command=run_encode)
encode_button.pack(side="left", padx=10)

decode_button = tk.Button(button_frame, text="Decode", command=run_decode)
decode_button.pack(side="left", padx=10)

quit_button = tk.Button(button_frame, text="Quit", command=root.destroy)
quit_button.pack(side="bottom", pady=10)

# Output text
output_label = tk.Label(root, text="", wraplength=350, fg="black")
output_label.pack(pady=20)

root.mainloop()
