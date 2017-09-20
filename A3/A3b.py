#Assignment 3 question 1
#By Alex Seppala 10132889 13as191
#and Angus Short 10135024 13ajs11

import re

def main():
    decoded = decode(importData_string("Mystery.txt"), importData_dictionary("Dictionary.txt"))#calls the decode function with the imported and formatted files as parameters
    write_data("output", decoded)#writes the decoded message to a text file
    print(decoded)

def decode(coded_string, decoder):
    buffer = ""#this is the temporary buffer that will be filled until a recognizable code is found, then it will be reset to ""
    output = ""#this will be populated and returned
    while len(coded_string) > 0:#iterates through each value in the coded string
        # print(len(coded_string))#this prints to show progess when it is executed
        buffer = buffer + coded_string[0]#adds the current code character to the buffer
        coded_string = coded_string[1:]#removes the current code character from the coded string
        if buffer in decoder:#if the buffer contains a code recognized in the dictionary
            output = output + decoder[buffer]#add the decoded character to the output string, the buffer is used as a key in the decoder dictionary, which maps to a character
            buffer = ""#reset the buffer
    return output

def write_data(filename, contents):#creates a text file and writes a string to it
    f = open(filename, 'w')
    f.write(contents)
    f.close

def importData_dictionary(filename):
    data = {}
    file = open(filename, 'r')
    while True:
        y = file.readline()#reads each line of the file
        if y == '':
            break
        lineData = re.split(' |\n',y)
        if lineData[1] == "":#special case for the space character
            data[lineData[2]] = " "#sets the space as space correctly
        elif lineData[0] == "<LF>":#special case for the line feed character
            data[lineData[1]] = '\n'#sets the line feed as newline
        else:
            data[lineData[1]] = lineData[0]#assigns the key and value in the dictionary for decoding
    file.close()
    return data

def importData_string(filename):#imports a text file as a string
    with open(filename, 'r') as myfile:
        data = myfile.read()
    return data

main()