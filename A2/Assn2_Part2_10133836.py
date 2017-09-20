'''
CMPE 380
Assignment #2 - Graph Coloring Part 2
Completed By: Mohamad Mansour
Student Number: 10133836
Completed using Python v2.7.12

Program Description:
The program makes use of the pseudocode provided to us in Week 4 Lab Problem's description.
To be able to determine the minimum number of tables required to seat everyone such that
no conflicts occur. Initially, each node's color is assigned to -1. Then the vertices are
sorted based on the number of neighbours it has in descending order. The sorted list is
then run through by assigning each vertex the small color (colors are defined from 1 to 30),
that has not been picked for one of its neighbours. This is done until the whole list has
run through. Once this is complete, the largest color used is returned, which defines
the least number of tables required.
I've determined the complexity of this program to be O(n^4) as I used 4 for loops.
'''

#Function to determine the least number of tables required.
def easyColor(graph, numberOfVertices):
    
    sortedVals = []         #Initally list of elements that will be sorted   
    length = {}             #Dictionary containing the number of neighbours each vertex has
    coloredNodes = {}       #Dctionary containing which color belongs to each vertex
    maximumVal = -1         

    #For loop used to set each vertex color to -1, add the vertex
    #values to sortedVals, and save the number of neighbours each vertex has.
    for elem in graph:
        coloredNodes[elem] = -1
        sortedVals.append(elem)
        length[elem] = len(graph[elem])

    #While loop that implements bubble sort to sort the vertices by descending number of neighbours 
    while True:
        swapped = -1        #Flag to keep track if sort occured.
        for i in range(0, len(graph)-1):
            if length[sortedVals[i+1]]>length[sortedVals[i]]:
                temp = sortedVals[i]
                sortedVals[i] = sortedVals[i+1]
                sortedVals[i+1] = temp
                swapped = 1
        if swapped == -1:   #If no sort occured, then sorting is complete
            break

    #For loop to assign each vertex the smallest unused color from each of the vertice's neighbours.
    for elem in sortedVals:
        listOfColors = range(1,31)
        for connected in graph[elem]:
            if coloredNodes[int(connected)] in listOfColors:
                listOfColors.remove(coloredNodes[int(connected)])
            coloredNodes[elem] = listOfColors[0]
            if maximumVal < listOfColors[0]:
                maximumVal = listOfColors[0]
         
    return maximumVal       #Minimum number of tables required is returned.

#Importing Graph 3
g3 = open('Graph3.txt', 'r')
graphThreeData = {}
g3NumberOfVertices = int(g3.readline().strip())
while True:                         #Read file and insert connected nodes in list of dictionary
    line = g3.readline()
    if line == '':                  #If line is empty, break
        break
    line = line.split()
    line.pop(1)                     #Removes ':' from line read
    graphThreeData.setdefault(int(line[0]), [])
    for i in range(1, len(line)):
        graphThreeData[int(line[0])].append(line[i])
g3.close()

#Importing Graph 4
g4 = open('Graph4.txt', 'r')
graphFourData = {}
g4NumberOfVertices = int(g4.readline().strip())
while True:                         #Read file and insert connected nodes in list of dictionary
    line = g4.readline()
    if line == '':                  #If line is empty, break
        break
    line = line.split()
    line.pop(1)                     #Removes ':' from line read
    graphFourData.setdefault(int(line[0]), [])
    for i in range(1, len(line)):
        graphFourData[int(line[0])].append(line[i])
g4.close()

#Importing Graph 5
g5 = open('Graph5.txt', 'r')
graphFiveData = {}
g5NumberOfVertices = int(g5.readline().strip())
while True:                         #Read file and insert connected nodes in list of dictionary
    line = g5.readline()
    if line == '':                  #If line is empty, break
        break
    line = line.split()
    line.pop(1)                     #Removes ':' from line read
    graphFiveData.setdefault(int(line[0]), [])
    for i in range(1, len(line)):
        graphFiveData[int(line[0])].append(line[i])
g5.close()

### Main Program ###

print "CMPE 380"
print "Assignment #2 - Graph Coloring"
print "Completed By: Mohamad Mansour"
print "Student Number: 10133836"
print "Completed using Python v2.7.12 \n"

print "The minimum number of tables required to sort Graph 3 is %d tables.\n" %easyColor(graphThreeData, g3NumberOfVertices)
print "The minimum number of tables required to sort Graph 4 is %d tables.\n" %easyColor(graphFourData, g4NumberOfVertices)
print "The minimum number of tables required to sort Graph 5 is %d tables." %easyColor(graphFiveData, g5NumberOfVertices)
