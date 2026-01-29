from bitwise import bitwise_hamming
from main import *
import timeit
import random
random.seed(0)

"""before running a time test, please make sure the value of r and the message in main.py and the message in bitwise.py are the same for a fair comparison"""

def run_bitwise():
    bitwise_hamming()

def run_matrix():
    main()

bitwise_time = timeit.timeit("run_bitwise()", globals=globals(), number=1000)
matrix_time = timeit.timeit("run_matrix()", globals=globals(), number=1000)

time_difference = matrix_time/bitwise_time

print(f"Bitwise time: {round(bitwise_time, 4)} seconds")
print(f"Matrix time:  {round(matrix_time, 4)} seconds")
print(f"Bitwise operations are {round(matrix_time/bitwise_time, 2)}× faster than matrix operations")