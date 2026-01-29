# Final Project Hamming
Our Programming for Mathematics Final Project.

## Description

This project implements a Hamming(7,4) encoder and decoder, with the option to generalize to Hamming(n,k) for any number of parity bits. When running main.py the user will be greeted with a popup window, our GUI, where they can enter a text message. The program will convert the text to binary, convert it into a matrix, simulate a random error, correct the message and decode it again, showing the user the same output they entered in the GUI. 
To switch between Hamming(7,4) and other Hamming(n,k) codes, you can change the r variable (number of parity bits) in main.py. The default is r=3, r=4 will give you a Hamming(15,11) code; r=5 will give you a Hamming(31,26) code; etc. We refer to our project report for a more detailed explanation of the algorithm and design choices. How to install and execute the code be found down below.

## Getting Started

Before you get started make sure you have the latest version of Python: Python 3.14.0.

For the unit tests you need to make sure you have pytest installed
To verify if pytest is installed, run ```pytest --version``` in the command terminal
If pytest is not yet installed, run ```pip install pytest``` in the command terminal
If that does not work, run ```python -m pip install pytest``` in the command terminal

### Installing

* Go to the main page of this repository.
* Click on the bright green button in the top right that says Code
* Select download as zip
* Unzip the files into a single folder

### Folder structure
"""
FinalProjectHamming/
├── main.py                  # Runs the GUI
├── window.py                # GUI implementation
├── encoderFunctions.py      # Encoding functions
├── errorCreation.py         # Introduces random error
├── decoderFunctions.py      # Decoding functions
├── matrixMakers.py          # Builds G,H,R matrices
├── Matrixclass.py           # Custom Matrix class
├── bitwise.py               # Bitwise implementation
├── test_hamming.py          # Unit tests general Hamming code
├── test_hamming_74.py       # Unit tests Hamming(7,4) code
└── test_time.py             # Time comparison matrix and bitwise implementation
"""

### Executing program

** Running the main file:
* Download and install the files as described
* Run main.py
* Enter a message in the GUI window
* Click the button to encode and decode your message
* Exit the program with the Quit button

** Running the unit tests:
* For Hamming(7,4) tests, open test_hamming_74.py
* Paste the following command into the terminal to run the test: ```py -m pytest test_hamming_74.py```
* Results will be printed to the terminal

* For general Hamming tests, open test_hamming.py
* Change the value of r to your desired number of parity bits
* Paste the following command into the terminal to run the test: ```py -m pytest test_hamming.py```
* Results will be printed to the terminal
## Authors

* Nicky Kroon (3342115)
* Madelief Mols (9423117)
* Cornelis Roepke (8798133)
