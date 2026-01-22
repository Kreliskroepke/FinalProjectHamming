from decoderfunctions import * #contains: decode, correct, position, convert_to_string, is_zero_matrix
from encoderfunctions import * #contains: encode, binaryconvert
from errorCreation import random_error
from main import main
from Matrixclass import Matrix
from matrixmakers import * #contains: G_matrix, H_matrix, R_matrix

#om te gebruiken plak in terminal: py -m pytest test_hamming.py

r = 3
G = G_matrix(r)
G_t = G.transpose()
H = H_matrix(r)
R = R_matrix(r)

def matrix_test(matrix):
    comparison_list = [m.vorm for m in matrix]
    return comparison_list


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
    assert decode(encode("hi", G_t), H, R) == "hi"
    assert decode(encode("roomba is stuck on the carpet", G_t), H, R) == "roomba is stuck on the carpet"
    assert decode(encode("0", G_t), H, R) == "0"
    assert decode(encode("1a+2bc", G_t), H, R) == "1a+2bc"
    assert decode(encode("programming for mathematics", G_t), H, R) == "programming for mathematics"
    assert decode(encode("1200+234567=9999887?", G_t), H, R) == "1200+234567=9999887?"