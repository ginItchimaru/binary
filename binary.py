#!/usr/bin/env python3

import sys


def int_to_binary(x):

    return bin(int(x))


def binary_to_int(x):
    
    return int(str(x), 2)



def input():

    if len(sys.argv) != 3:
        
        print("Usage: binary.py -b/-i number\n-i for integer input\n-b for binary input")
        sys.exit(1)

    specifier = sys.argv[1]
    number = int(sys.argv[2])

    if specifier == "-i":

        print(int_to_binary(number))

    elif specifier == "-b":

        print(binary_to_int(number))

    else:

        print("Usage: binary.py -b/-i number\n-i for integer input\n-b for binary input")



if __name__ == '__main__':

    input()
