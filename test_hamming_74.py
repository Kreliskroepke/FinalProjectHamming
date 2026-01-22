from decoderfunctions import * #contains: decode, correct, position, convert_to_string, is_zero_matrix
from encoderfunctions import * #contains: encode, binaryconvert
from errorCreation import random_error
from main import main
from Matrixclass import Matrix
from matrixmakers import * #contains: G_matrix, H_matrix, R_matrix

"""
this test only works for r=3, to test values of r > 3 please use test_hamming.py
om te gebruiken plak in terminal: py -m pytest test_hamming.py
"""

r = 3 
G = G_matrix(r)
G_t = G.transpose()
H = H_matrix(r)
R = R_matrix(r)

def matrix_test(input_matrix):
    return [m.vorm for m in input_matrix]
    
def list_test(input_list):
    return [Matrix(m) for m in input_list]

def test_encode():
    #test hi
    actual_hi = matrix_test(encode("hi", G_t))
    expected_hi = [
        [[1], [1], [0], [0], [1], [1], [0]],
        [[1], [1], [1], [0], [0], [0], [0]],
        [[1], [1], [0], [0], [1], [1], [0]],
        [[0], [0], [1], [1], [0], [0], [1]]
    ]
    assert actual_hi == expected_hi

    #test roomba
    actual_roomba = matrix_test(encode("roomba", G_t))
    expected_roomba = [
        [[0], [0], [0], [1], [1], [1], [1]],
        [[0], [1], [0], [1], [0], [1], [0]],
        [[1], [1], [0], [0], [1], [1], [0]],
        [[1], [1], [1], [1], [1], [1], [1]],
        [[1], [1], [0], [0], [1], [1], [0]],
        [[1], [1], [1], [1], [1], [1], [1]],
        [[1], [1], [0], [0], [1], [1], [0]],
        [[1], [0], [1], [0], [1], [0], [1]],
        [[1], [1], [0], [0], [1], [1], [0]],
        [[0], [1], [0], [1], [0], [1], [0]],
        [[1], [1], [0], [0], [1], [1], [0]],
        [[1], [1], [0], [1], [0], [0], [1]]
    ]
    assert actual_roomba == expected_roomba

    #test 0
    actual_zero = matrix_test(encode("0", G_t))
    expected_zero = [
        [[1], [0], [0], [0], [0], [1], [1]], 
        [[0], [0], [0], [0], [0], [0], [0]]
        ]
    assert actual_zero == expected_zero

    #test 1+2
    actual_plus = matrix_test(encode("1+2", G_t))
    expected_plus = [
        [[1], [0], [0], [0], [0], [1], [1]], 
        [[1], [1], [0], [1], [0], [0], [1]], 
        [[0], [1], [0], [1], [0], [1], [0]], 
        [[0], [1], [1], [0], [0], [1], [1]], 
        [[1], [0], [0], [0], [0], [1], [1]], 
        [[0], [1], [0], [1], [0], [1], [0]]
        ]
    assert actual_plus == expected_plus

def test_random_error():
    assert random_error(encode("hi", G_t)) != encode("hi", G_t)
    assert random_error(encode("roomba is stuck on the carpet", G_t)) != encode("roomba is stuck on the carpet", G_t)
    assert random_error(encode("hi", G_t)) != encode("hi", G_t)

def test_decode():
    # test math
    input_list = [
        [[1], [0], [0], [0], [0], [1], [1]], 
        [[0], [1], [0], [1], [0], [1], [0]], 
        [[1], [1], [0], [0], [1], [1], [0]], 
        [[0], [1], [1], [0], [0], [1], [1]], 
        [[1], [0], [0], [0], [0], [1], [1]], 
        [[0], [1], [0], [1], [0], [1], [0]], 
        [[1], [1], [0], [0], [1], [1], [0]], 
        [[0], [1], [1], [0], [0], [1], [1]]
    ]
    input_matrix = list_test(input_list)
    actual_math = decode(input_matrix, H, R)
    assert actual_math == "math"

    #test 00
    input_list = [
        [[1], [0], [0], [0], [0], [1], [1]], 
        [[0], [0], [0], [0], [0], [0], [0]], 
        [[1], [0], [0], [0], [0], [1], [1]], 
        [[0], [0], [0], [0], [0], [0], [0]]
    ]
    input_matrix = list_test(input_list)
    actual_zeroes = decode(input_matrix, H, R)
    assert actual_zeroes == "00"

    #test n!
    input_list = [
        [[1], [1], [0], [1], [0], [0], [1]], 
        [[0], [1], [0], [1], [0], [1], [0]], 
        [[1], [0], [0], [0], [0], [1], [1]], 
        [[0], [1], [1], [0], [0], [1], [1]], 
        [[1], [0], [0], [0], [0], [1], [1]], 
        [[0], [1], [0], [1], [0], [1], [0]], 
        [[1], [1], [0], [0], [1], [1], [0]], 
        [[0], [1], [1], [0], [0], [1], [1]]
    ]
    input_matrix = list_test(input_list)
    actual_n = decode(input_matrix, H, R)
    assert actual_n == "n!=6"


def test_entire_code():
    assert decode(random_error(encode("our code works!", G_t)), H, R) == "our code works!"
    assert decode(random_error(encode("math is underrated", G_t)), H, R) == "math is underrated"
    assert decode(random_error(encode("00000000", G_t)), H, R) == "00000000"
    assert decode(random_error(encode("i**2=-1", G_t)), H, R) == "i**2=-1"