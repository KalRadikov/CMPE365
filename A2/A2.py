import re

def main():
    importDataReturn = importData('Graph1.txt')
    # importDataReturn = importData('Graph2.txt')
    numberOfPeople = int(importDataReturn[0])
    DataStructure = initializeDataStructure(importDataReturn)
    DataStructure[1]["colour"] = 1
    #printDataStruct(numberOfPeople,DataStructure)
    twoColour(numberOfPeople,DataStructure)

    #for each of the vertices in order
        #check if any edge connected to this vertex is the same colour
            #if yes the end program and say table exceeds two
            #else colour each edge of this vertice to the other colour


def twoColour(numberOfPeople,DataStructure):
    for vertex in range(1,(numberOfPeople +1)):
        for edge in range(0,(len(DataStructure[vertex]["edges"]))):
            # print("vertex: ",vertex, " edge: ", edge )
            # print("vertex colour: ",DataStructure[vertex]["colour"], " edge colour: ", DataStructure[DataStructure[vertex]["edges"][edge]]["colour"])
            if(DataStructure[vertex]["colour"] == DataStructure[DataStructure[vertex]["edges"][edge]]["colour"]):
                print("two tables is not enough")
                return
            DataStructure[DataStructure[vertex]["edges"][edge]]["colour"] = 2 if (DataStructure[vertex]["colour"] == 1) else 1
    print("two tables is enough")
    return

def printDataStruct(numberOfPeople,DataStructure):
    for i in range(1,(numberOfPeople + 1)):
        print(DataStructure[i])

def initializeDataStructure(data):
    numOfPpl = int(data[0])
    print(numOfPpl)
    vertexEdges = data[1]
    for i in range(1,(numOfPpl + 1)):
        temp = vertexEdges[i]
        vertexEdges[i] = {"colour":0, "edges":temp}
    return vertexEdges


def importData(filename):
    data = {}
    file = open(filename, 'r')
    numberOfPeople = file.readline()
    while True:
        y = file.readline()
        if y == '':
            break
        lineData = re.split(', |\t|\n| : \t',y)
        lineData = lineData[:len(lineData) - 1]
        lineData = [int(x) for x in lineData]
        key = lineData.pop(0)
        data[key] = lineData
    file.close()
    return [numberOfPeople,data]

main()