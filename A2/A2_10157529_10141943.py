'''====================================================================================================================
 |   Assignment 2: Graph Colouring NPC Complete Problem
 |
 |   Authors:  Kaloyan Radikov 10157529
 |             Henley Chiu 10141943
 |
 |   Due Date:  Oct 20th 2016
 |
 *=================================================================================================================='''

import re

def main():

    numPeople = importPeople('Graph1.txt')
    dataStruct = importData('Graph1.txt')
    print("Number of people in Graph 1:", numPeople)
    twoColour(dataStruct)

    numPeople = importPeople('Graph2.txt')
    dataStruct = importData('Graph2.txt')
    print("Number of people in Graph 2:", numPeople)
    twoColour(dataStruct)

    dataStruct = importData('Graph3.txt')
    print("Least number of colours required for Graph 3:", easyColour(dataStruct), '\n')

    dataStruct = importData('Graph4.txt')
    print("Least number of colours required for Graph 4:", easyColour(dataStruct), '\n')

    dataStruct = importData('Graph5.txt')
    print("Least number of colours required for Graph 5:", easyColour(dataStruct))

def easyColour(dataStruct):

    # ---------------------------- Declaring variables to be used in the main for loop ------------------------------- #

    sortedVals = []  # Initially list of elements that will be sorted
    length = {}  # Dictionary containing the number of neighbours each vertex has
    coloredNodes = {}  # Dictionary containing which color belongs to each vertex
    maximumVal = -1
    
    for elem in dataStruct:
        coloredNodes[elem] = -1
        sortedVals.append(elem)
        length[elem] = len(dataStruct[elem])

    # ---------------------------- List of descending sorted keys from the dictionary -------------------------------- #

    sortedList = sorted(dataStruct, key=lambda k: len(dataStruct[k]), reverse=True)

    # ---------------------------- Main loop to find the max number of colours required ------------------------------ #

    for key in sortedList:
        listOfColors = list(range(1, 31))
        for val in dataStruct[key]:
            if coloredNodes[val] in listOfColors:
                listOfColors.remove(coloredNodes[val])
        coloredNodes[key] = listOfColors[0]
        if maximumVal < coloredNodes[key]:
            maximumVal = coloredNodes[key]

    return maximumVal



def twoColour(dataStruct):


    White = []
    Black = []

    Black.append(1)

    # ------------------------ Main loop to check the colour arrays and append neighbours  --------------------------- #

    for key in dataStruct:
        for vertex in dataStruct[key]:
            if key in Black:
                if key in White:
                    print('Graph cannot be 2 coloured\n')
                    return
                else:
                    White.append(vertex)

            elif key in White:
                Black.append(vertex)
            else:
                White.append(vertex)

    print("Graph can be 2 coloured\n")


def importData(filename):

    # ------------------------ Standard function used to import data, stores in dictionary --------------------------- #

    data = {}
    file = open(filename, 'r')
    while True:
        y = file.readline()
        if y == '':
            break
        lineData = re.split(', |\t|\n| : \t', y)
        lineData = lineData[:len(lineData) - 1]
        lineData = [int(x) for x in lineData]
        key = lineData.pop(0)
        data[key] = lineData
    file.close()

    data = initDict(data)

    return data

def printDict(Dict, num):

    # ------------------ Functioned used to print dictionaries. mainly used for troubleshooting ---------------------- #

    for i in range(1,num+1):
        print(Dict[i])

def importPeople(filename):

    # ------------------------- Importing the number of people or vertices in the graph ------------------------------ #

    file = open(filename, 'r')
    num = file.readline()
    file.close()
    num = int(num)
    return num

def initDict(my_dict):

    # ---------------------------- Function used to change the string values to ints --------------------------------- #

    output_dict = {}
    for key, value in my_dict.items():
        output_dict[int(key)] = [int(item) for item in value]
    return output_dict


def bubbleSort(dict):

    # ------------------ Used to sort a dictionary in descending order of degree for keys ---------------------------- #

    for i in dict:
        for j in range(i+1, len(dict)):
            if len(dict[j]) > len(dict[i]):
                dict[j], dict[i] = dict[i], dict[j]

main()
