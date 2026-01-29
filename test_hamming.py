from decoderFunctions import * #contains: decode, correct, position, convertToString, isZeroMatrix
from encoderFunctions import * #contains: encode, binaryConvert
from errorCreation import randomError
from main import main
from Matrixclass import Matrix
from matrixMakers import * #contains: G_matrix, H_matrix, R_matrix

r = 3 #change r to test different Hamming codes
G = G_matrix(r)
G_t = G.transpose()
H = H_matrix(r)
R = R_matrix(r)

def test_randomError():
    assert randomError(encode("hi", G_t)) != encode("hi", G_t)
    assert randomError(encode("roomba is stuck on the carpet", G_t)) != encode("roomba is stuck on the carpet", G_t)
    assert randomError(encode("hi", G_t)) != encode("hi", G_t)

def test_decode():
    assert decode(encode("hello world", G_t), H, R) == "hello world"
    assert decode(encode("0", G_t), H, R) == "0"
    assert decode(encode("1a+2bc", G_t), H, R) == "1a+2bc"
    assert decode(encode("programming for mathematics", G_t), H, R) == "programming for mathematics"
    assert decode(encode("1200+234567=9999887?", G_t), H, R) == "1200+234567=9999887?"

def test_entire_code():
    assert decode(randomError(encode("hej hej", G_t)), H, R) == "hej hej"
    assert decode(randomError(encode("don't stop me now!", G_t)), H, R) == "don't stop me now!"
    assert decode(randomError(encode("0", G_t)), H, R) == "0"
    assert decode(randomError(encode("1a+2bc=3pi", G_t)), H, R) == "1a+2bc=3pi"
    assert decode(randomError(encode("programming for mathematics is our #1 course", G_t)), H, R) == "programming for mathematics is our #1 course"
