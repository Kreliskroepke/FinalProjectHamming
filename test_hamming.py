from decoderfunctions import * #contains: decode, correct, position, convert_to_string, is_zero_matrix
from encoderfunctions import * #contains: encode, binaryconvert
from errorCreation import random_error
from main import main
from Matrixclass import Matrix
from matrixmakers import * #contains: G_matrix, H_matrix, R_matrix

"""
To use, paste the following into the terminal: py -m pytest test_hamming.py
"""

r = 3 #change r to test different Hamming codes
G = G_matrix(r)
G_t = G.transpose()
H = H_matrix(r)
R = R_matrix(r)

def test_random_error():
    assert random_error(encode("hi", G_t)) != encode("hi", G_t)
    assert random_error(encode("roomba is stuck on the carpet", G_t)) != encode("roomba is stuck on the carpet", G_t)
    assert random_error(encode("hi", G_t)) != encode("hi", G_t)

def test_decode():
    assert decode(encode("hello world", G_t), H, R) == "hello world"
    assert decode(encode("0", G_t), H, R) == "0"
    assert decode(encode("1a+2bc", G_t), H, R) == "1a+2bc"
    assert decode(encode("programming for mathematics", G_t), H, R) == "programming for mathematics"
    assert decode(encode("1200+234567=9999887?", G_t), H, R) == "1200+234567=9999887?"

def test_entire_code():
    assert decode(random_error(encode("hej hej", G_t)), H, R) == "hej hej"
    assert decode(random_error(encode("don't stop me now!", G_t)), H, R) == "don't stop me now!"
    assert decode(random_error(encode("0", G_t)), H, R) == "0"
    assert decode(random_error(encode("1a+2bc=3pi", G_t)), H, R) == "1a+2bc=3pi"
    assert decode(random_error(encode("programming for mathematics is our #1 course", G_t)), H, R) == "programming for mathematics is our #1 course"
