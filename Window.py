import tkinter as tk
from encoderfunctions import *
from decoderfunctions import *
from Matrixclass import Matrix
from matrixmakers import * #contains: G_matrix, H_matrix, R_matrix

"""
Notes:
1) ik heb even gegoogled en als ik het goed begrijp kunnen we dit heel makkelijk in main integreren door in main te zetten:
if __name__ == "__main__":
    windowmaker()
dan als je main runt open je windowmaker en als we testen runt ie gewoon de code (en negeert ie window maker). dus het blijven twee aparte bestanden
2) dan moet nog wel de windowmaker werken, haha, daarvoor moeten we: 
- de matrixen ook hierin maken en meegeven aan encode en decode (zoals in main)
- via log-functies kun je tussentijdse resultaten laten zien, maar dit snap ik nog niet helemaal...
zie bijvoorbeeld: https://stackoverflow.com/questions/13318742/python-logging-to-tkinter-text-widget en https://tkdocs.com/tutorial/text.html (logging window)
volgens mij moeten we in de codes waar we iets willen laten zien (encode, random_error, decode) een logger maken en dan in windowmaker moet er ook iets gebeuren (dat is dan volgens mij logging window)??
"""
def Windowmaker():
    
    r = 3 #aantal parity bits
    
    G = G_matrix(r)
    G_t = G.transpose()
    H = H_matrix(r)
    R = R_matrix(r)

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
    
        #Output text
        output_label = tk.Label(root, text="", wraplength=350, fg="black")
        output_label.pack(pady=20)
    
        root.mainloop()
