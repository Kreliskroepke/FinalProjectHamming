import tkinter as tk
import tkinter.font as tkfont #change fonttype
from tkinter import scrolledtext #get a scrollbar on textblocks
from encoderfunctions import *
from decoderfunctions import *
from Matrixclass import Matrix
from matrixmakers import * #contains: G_matrix, H_matrix, R_matrix

def Windowmaker():
    
    r = 3 #aantal parity bits
    
    G = G_matrix(r)
    G_t = G.transpose()
    H = H_matrix(r)
    R = R_matrix(r)
    k = G_t.kolommen

    def run_code():
        """This takes a string, and returns the result + in-betweens"""
        user_input = entry.get()
        if not user_input.strip():
            #state="normal" maakt de textbox editable
            output_text.config(state="normal")
            #delete everything from row 1 char 0 to end
            output_text.delete("1.0", tk.END)
            #add the text at the end (if removing tk.END it broke)
            output_text.insert(tk.END, "Please fill in a message.")
            output_text.config(state="disabled")
            return
        result = tussenstappen(user_input, G_t)
        formatted = formatting(result)
        
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, formatted)
        output_text.config(state="disabled")

    def tussenstappen(a, G_t):
        """Very slow way to get all in-between steps"""
        binary = binaryconvert(a,k)
        readableBinary = readableEncoder(binary)
        encodedmessage = encode(a, G_t)
        decodedmessage = decode(encodedmessage, H, R)
        return(dict(YourMessageInBinary=readableBinary, EncodedMessage=encodedmessage, YourDecodedMessage=decodedmessage))

    def formatting(data):
        """This makes the text readable in the GUI"""
        lines = []
        lines.append("Your message in binary:")
        lines.append(data["YourMessageInBinary"])
        lines.append("")

        lines.append("Your encoded message in a matrix:")
        for i, block in enumerate(data["EncodedMessage"], start=1):
            lines.append(f"{block}")
        lines.append("")
        lines.append("Your decoded message:")
        lines.append(str(data["YourDecodedMessage"]))

        return "\n".join(lines)
        
    #Create popup window
    root = tk.Tk()
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.config(family="Times New Roman", size=11)
    root.title("Hamming Code")
    root.config(bg="#ead78d")
    root.geometry("600x450")
    root.configure(bg="#ead78d")

    #Text at top
    title_label = tk.Label(root, text="Welcome to our Hamming en-/decoder!")
    title_label.pack(pady=10)
    title_label.config(bg="#ead78d")
    expl_label = tk.Label(root, text="Give your message, and click the run button.")
    expl_label.pack(pady=0)
    expl_label.config(bg="#ead78d")

    #Input field
    entry = tk.Entry(root, width=40)
    entry.pack(pady=5)
    
    #Buttons frame
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)
    button_frame.config(bg="#ead78d")

    main_button = tk.Button(button_frame, text="Run the code!", command=run_code)
    main_button.pack(side="left", padx=10)
    main_button.config(bg="#748E61", fg="#ffffff")

    quit_button = tk.Button(button_frame, text="Quit", command=root.destroy)
    quit_button.pack(side="bottom", pady=10)
    quit_button.config(bg="#748E61", fg="#ffffff")
    
    #Create a textbox to display everything
    output_text = scrolledtext.ScrolledText(root, width=70, height=15, wrap="word")
    output_text.pack(pady=20)
    output_text.config(bg="#d4bd82")
    output_text.config(state="disabled")
    
    root.mainloop()

Windowmaker()
