'''---------------------------------------------------------------------------------------------------------------------

CMPE 365 ASSIGNMENT 3 - APPLYING HUFFMANS ALGORITHM TO A TEXT BASE FILE
NAMES: KAL RADIKOV 10157529 || HENLEY CHIU 10141943
DATE: NOVEMBER 7ST 2016

---------------------------------------------------------------------------------------------------------------------'''
import re
import time

''' ------------------------------------------------- Part 1 ------------------------------------------------------- '''

def main():

    numChar = 0
    numEncode = 0
    freqLetters = {}

# ---------------------- Finding frequency of each unique letter in the SamMcGee text file --------------------------- #

    with open("SamMcGee.txt", "r", encoding='utf-8') as f:
        for line in f:
            for c in line:
                if c not in freqLetters:
                    freqLetters[c] = 1
                else:
                    freqLetters[c] += 1

# ------------------------------- Also keeping track of number of character ------------------------------------------ #
                numChar += 1

    freqCopy = freqLetters.copy()
    bitstring = huffman(freqCopy)

# -------------------------- Counting total bits needed to encode the text file -------------------------------------- #

    for i in freqLetters:
        numEncode += (freqLetters[i] * len(bitstring[i]))

# ------------------------------- For fun: calculated total space saved ---------------------------------------------- #

    memPercent = (1-(numEncode/(numChar*8)))

# ----------------------------------- Printing statements. Note: 8 bits in a char ------------------------------------ #

    print("Assuming each character in the file is 1 byte,\nTotal number of bits needed to store file is:", numChar*8)
    print("\nUsing the Huffman encoding algorithm,\nTotal number of bits needed to store file is:", numEncode)
    print("\nThis provides a decrease in filesize of:", round(memPercent, 2), "%")

''' ------------------------------------------------- Part 2 ------------------------------------------------------- '''

# -------------------------------------- Opening bitstring file to be decoded ---------------------------------------- #

    with open('Mystery.txt', 'r') as file:
        bitstring = file.read()

# ------------------------------- Importing Dictionary.txt into python dictionary ------------------------------------ #

    Dictionary = {}
    file = open('Dictionary.txt', 'r')
    while True:
        y = file.readline()
        if y == '':
            break
        lineData = re.split(' |\n', y)
        if lineData[1] == "":
            Dictionary[lineData[2]] = " "
        elif lineData[0] == "<LF>":
            Dictionary[lineData[1]] = '\n'
        else:
            Dictionary[lineData[1]] = lineData[0]
    file.close()

# --- Setting the buffer which will hold unique string of bits that were appended to be matched with the dictionary -- #

    decode = ""
    buffer = ""

# -------------------------- Taking one bit at a time and trying to match with dictionary ---------------------------- #

    while (len(bitstring) > 0):

        buffer += bitstring[0]
        bitstring = bitstring[1:]
        if buffer in Dictionary:
            decode += Dictionary[buffer]
            buffer = ""

    print ("\n\n>> Sending decoded file to 'Output' and printing decoded file")
    time.sleep(5)

# ------------------------------ Creating a text file and printing output to it -------------------------------------- #

    text_file = open("Mystery_Output", "w")
    text_file.write(str(decode))
    text_file.close()

# --------------------- Printing the string of letters decoded from the bitstring ------------------------------------ #

    print(decode)

# ----------------------------------------------- Functions ---------------------------------------------------------- #

def huffman(dict):

# - Building the tree as a dictionary where left and right bitstrings will be stored. Highest frequency = less bits -- #

    dictCopy = dict
    R = {}
    bitstring = {}
    for elem in dict:
        R[elem] = [elem]
        bitstring[elem] = ''
    while len(dictCopy) > 1:
        left = min(dict, key=dict.get)
        f = dict[left]
        dictCopy.pop(left)
        right = min(dict, key=dict.get)
        f = f + dict[right]
        dictCopy.pop(right)
        LR = left + right
        dictCopy[LR] = f
        R[LR] = R[left] + R[right]

# ------------------- Appending 0 or 1 depending if leftChild or RightChild to create correct encoding --------------- #

        for i in R[left]:
            bitstring[i] = '0' + bitstring[i]

        for i in R[right]:
            bitstring[i] = '1' + bitstring[i]

    return bitstring


main()