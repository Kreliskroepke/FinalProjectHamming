from encoderfunctions import binaryconvert
import random

def bitwise_hamming():
    """encodes, checks, corrects and decodes a message using bitwise operators"""
    r = 3
    n = 2**r -1	
    k = n - r 
    
    #parity and data positions
    parity_positions = [2**p for p in range(r)] #1,2,4,...
    data_positions = [d for d in range(1,n+1) if d not in parity_positions] #3,5,6,7,...
  
    #message to be sent
    message = "bit+wise-operator101"
    knabbellijst = binaryconvert(message,k)
    
    #encoding message
    codemessages = []
    for knabbel in knabbellijst:
        codemessage = [0]*n
        for data in range(k):
            codemessage[data_positions[data]-1] = knabbel[data]
        for p in parity_positions:
            xor_sum = 0 
            for d in range(1,n+1):
                if d & p: #AND to check if p and d have 1 in same bit position in binary, for parity_i that is position -i
                    xor_sum ^= codemessage[d-1] #if data bit and parity bit match, XOR to add 1 (modulo 2)
            codemessage[p-1] = xor_sum
        codemessages.append(codemessage)
   
    #error in random message on a random position
    codemessage = random.choice(codemessages)
    error = random.randrange(n)
    codemessage[error] ^= 1 #XOR to flip the bit

    #receiving and checking message
    for codemessage in codemessages:
        position =0
        position_vector = []
        for p in parity_positions:
            xor_sum = 0 
            for d in range(1,n+1):
                if d & p: 
                    xor_sum ^= codemessage[d-1]  
            position_vector.append(xor_sum)
        for i, pbit in enumerate(position_vector):
            position |= (pbit << i) #left shift pbit to correct binary position, OR to set bit in position
        
    #correcting the message
        if position != 0:
            codemessage[position-1] ^= 1
    
    #decoding
    receivedmessages =[]
    for codemessage in codemessages:
        receivedmessage = [codemessage[dbit-1] for dbit in data_positions]
        receivedmessages.append(receivedmessage)
    
    binarymessage = ""
    for receivedmessage in receivedmessages:
        binarymessage += "".join(str(bit) for bit in receivedmessage)

    decodedmessage = ""
    b = k if k > 8 else 8 
    for i in range(0, len(binarymessage), b):
            byte = binarymessage[i:i+b]
            decodedmessage += chr(int(byte, 2))
