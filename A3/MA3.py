'''
CMPE 380
Assignment #3 - Huffman Coding - Part 1
Completed By: Mohamad Mansour
Student Number: 10133836
Completed using Python v2.7.12

Program Description: This program makes use of the Huffman coding algorithm to code
the given text file into bitstrings. This is done by first calculating the frequency
of each character. The characters with the two lowest frequencies are then grouped
together until a tree is created. We make sure to pop the two lowest elements as to
not repeat them in the tree. While this is happening, the left side of each node
of the tree is given a 0 and the right side is given a 1.
At the end, a bitstring dictionary of each character is returned and this allows us
to calculate the number of bits required using the algorithm to compare it to the
number of bits required if we were to use 8 bits for each character.
'''

# Import 'open' to be able to encode the textfile into unicode.
from io import open

# Variable initilizations
frequencies = {}
numCharacters = 0  # Number of characters in text file.
numHuffman = 0  # Used to store the number of bits needed if coded in Huffman


# Function used to calculate the Huffman code of each character given each character's frequency
def huffmanCoding(frequencies):
    W = frequencies  # Working space
    R = {}  # Used to build the tree
    bitstring = {}  # Used to store the bitstrings of each character
    for elem in frequencies:  # Initialize the tree and bitstring dictionaries
        R[elem] = [elem]
        bitstring[elem] = ''  # Initially, bitstring is empty for each character
    while len(W) > 1:  # While we still have character, we haven't used, looped
        left = min(frequencies, key=frequencies.get)  # Set character with minimum frequency to left node
        f = frequencies[left]  # Save its frequency
        W.pop(left)  # Remove it from the working space
        right = min(frequencies, key=frequencies.get)  # Set character with minimum frequency to right node
        f = f + frequencies[right]  # Add its frequency to the left node
        W.pop(right)  # Remove it from the working space
        LR = left + right  # Concatenate the letters of the two nodes
        W[LR] = f  # Add the concatenated letters to the working space
        R[LR] = R[left] + R[right]  # Add the concatenated letters to the tree

        for elem in R[left]:  # Assign 0 to the bitstring of the left characters
            bitstring[elem] = '0' + bitstring[elem]

        for elem in R[right]:  # Assign 1 to the bitstring of the right characters
            bitstring[elem] = '1' + bitstring[elem]
    return bitstring


# Open text file, and store each character with its frequencies in a dictionary
# file = open('SamMcGee.txt', 'r', encoding='utf-8')
# while 1:
#     char = file.read(1)  # Read 1 character at a time
#     if not char: break  # If not character, you have finished reading the file
#     if char in frequencies.keys():
#         frequencies[char] = frequencies[char] + 1
#     else:
#         frequencies[char] = 1
#     numCharacters = numCharacters + 1  # Save the number of characters in the file
with open("SamMcGee.txt", "r", encoding='utf-8') as f:
    for line in f:
        for c in line:
            if c not in frequencies:
                frequencies[c] = 1
            else:
                frequencies[c] += 1
        numCharacters += 1
f.close()
print(frequencies)

freq = frequencies.copy()  # Create a copy of the frequency dictionary before it is used in the Huffman Coding function
# It is used later to calculate the number of bits required for each character
bitstring = huffmanCoding(frequencies)  # Run the Huffman Coding algorithm

print(bitstring)

for elem in freq:  # Calculate number of bits required if each character is stored using it's bitstrings from the algorithm
    numHuffman = numHuffman + (freq[elem] * len(bitstring[elem]))
print ("The number of bits required if each character is stored using Huffman coding:", numHuffman)


