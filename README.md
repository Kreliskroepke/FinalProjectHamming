# Final Project Hamming
Our Programmeren voor Wiskunde Final Project.

## Description

This project runs a Hamming(7,4) encoder and decoder. When opened you will be greeted with a popup window, our GUI, where you can fill in some text, and it will generate the text in binary, convert it into a matrix, and then simulates a random error, and then returns the output of our code, which will be the same as the input. To change the Hamming(7,4) to a general Hamming(n,k) code, change the r variable in main.py. r=4 will give you a Hamming(15,11) code; r=5 will give you a Hamming(31,26) code; etc, etc. We refer to our report on this project for any further explanation of our code, and we refer to the installing and executing down below.

## Getting Started

To get started make sure you have the latest version of Python: Python 3.14.0.

For the unit tests you need to make sure you have piptest installed.
To verify if pytest is installed, run ```pytest --version``` in the command terminal.
If pytest is not yet installed, run ```pip install pytest``` in the command terminal.
If that does not work, run ```python -m pip install pytest``` in the command terminal.

### Installing

* Go to the main path of this project.
* Click on the bright green button in the top right that says Code
* Press download as zip

### Executing program

** Running the main file:
* Download all the files as a zip, as seen in Installing.
* Unzip the files into a single folder.
* Run main.py and press on the arrow.
* Fill in a message.

** Doing the unit tests:
* For Hamming(7,4) tests, open test_hamming_74.py
* Paste the following command into the terminal: py -m pytest test_hamming_74.py
```
py -m pytest test_hamming_74.py
```

* For general Hamming tests, open test_hamming.py
* Paste the following command into the terminal: 
```
py -m pytest test_hamming.py
```

## Authors

* Nicky Kroon (3342115)
* Madelief Mols (9423117)
* Cornelis Roepke (8798133)
