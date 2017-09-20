'''
CMPE 380
Assignment #4
Completed By: Mohamad Mansour
Student Number: 10133836
Completed using Python v2.7.12

Program Description: This program makes use of recurrence relations. It is programmed
using for loops. Initially each of the project files are imported into dictionaries.
Each project file's dictionary is then used to be able to determine the max income
that can be recived based on the projects. This is done by going through all the
projects for every week of the number of weeks. If the end week of a project is less
than or equal to the current week, then this project is a possible source of income.
You then check the income based on selected this project compared to previously
seen projects. This is repeated and at the end you have the maximum income possible
for each week.
By using this information and the last project used in each week, you are able
to figure out the path to get the maximum income. This is then printed to an
output file where the results can be analzyed.
'''

### Functions Used ###

#Function used to import projects from a file.
#Returns a dictionary with the number of projects, number of weeks,
#and each project's start week, duration and value.
def openProject(fileName):
    file = open(fileName, 'r')
    projects = {}
    projects['numWeeks'] = int(file.readline())                 #Number of weeks line is read.
    projects['numProjects'] = int(file.readline())              #Number of projects line is read.
    for i in range(0,projects['numProjects']):                  #For each of the projects, use the project number,
        project = file.readline()                                   #as the key of the project dictionary, and the value
        properties = project.split()                                #of the key would be the project's start week, duration,
        projectNumber = properties[0]                               #and value.
        del properties[0]
        projects[int(projectNumber)] = map(int, properties)    #Changes the strings to integers
    file.close()
    return projects                                             #Return dictionary of projects.

#Function used to return the max income that can be returned from each project file
#along with the specific projects to be selected to achieve this income.
def maxRevenue(projectFiles):
    numWeeks = projectFiles['numWeeks']                         #Retrieve number of weeks.
    numProjects = projectFiles['numProjects']                   #Retrieve number of projects.
    profit= {}                                                  #Dictionary used to hold the profit of each week.
    lastProject= {}                                             #Dictionary used to hold the last project used for each week.
    for week in range(1, numWeeks+1):                           #For every week
        if week not in profit.keys():                           #If the week does not have profit yet, set it's profit as 0.
            profit[week]= 0
        for project in range(1,numProjects+1):                  #For every project,
            startWeek = projectFiles[project][0]                #Save values as variabels to be used later (to make code easier to read)
            duration = projectFiles[project][1]
            value = projectFiles[project][2]
            endWeek = startWeek + duration - 1
            if endWeek <= week:                                 #Only consider project if its end week is less than or equal to the current week
                if projectFiles[project][0] == 1:               #If the project's start week is week 1, then it's value until now, is its value.
                    possibleProfit = value
                else:
                    possibleProfit = value + profit[startWeek-1]    #Otherwise, the week's value is the project's value plus the value of the up until the week before it starts
                profit[week]= max(profit[week],possibleProfit)
                if profit[week] == possibleProfit:              #If the profit of the current week is equal to the profit when using this project, then this project is the last project used
                    lastProject[week] = project
    maxProfit = profit[max(lastProject)]                        #Max income is the max value of each week's profit
    lastP = lastProject[max(lastProject)]                       #Last project used of the max profit week
    results = []                                                #List used to store the path to reach maximum income.

    while 1:                                                    #Loop until income = 0
        results.append(lastP)                                       #Retrieves path to get to max income value by backtracing steps.
        maxProfit = maxProfit - projectFiles[lastP][2]          #Subtract last project's value and check if its zero.
        if maxProfit == 0:                                    #If income = 0, break
            break
        for weeks in profit:                                    #If not zero, then find the week with the same income and retrieve that week's last project and loop until path found.
            if profit[weeks] == maxProfit:
                week = weeks
        lastP = lastProject[week]
    results.reverse()                                           #Reverse results list as they were inserted from end to beginning.
    print (resultsFile, "Path: ",)                            #Print path to output file
    for i in range(0,len(results)-1):                           #Print each step of the path with an arrow except last step
        print >> resultsFile, results[i],
        print >> resultsFile, " -> ",
    print >> resultsFile, results[len(results)-1]               #Print last step of path
    print >> resultsFile, ""                                    #Skip line for next project
    return 0

### Main Code ###

resultsFile = open('outputResults.txt', 'w')                    #Open text file to place results

#Load project files
projectOneFiles = openProject('Qooqle_Projects_8_6_1477962811.78.txt')
projectTwoFiles = openProject('Qooqle_Projects_10_30_1477962181.44.txt')
projectThreeFiles = openProject('Qooqle_Projects_52_150_1477962917.86.txt')
projectFourFiles = openProject('Qooqle_Projects_500_1500_1477962966.94.txt')

print(projectOneFiles)

# #Print results
# print >> resultsFile, "CMPE 380"
# print >> resultsFile, "Assignment #4"
# print >> resultsFile, "Completed By: Mohamad Mansour"
# print >> resultsFile, "Student Number: 10133836"
# print >> resultsFile, "Completed using Python v2.7.12 \n"
#
# print >> resultsFile, "The maximum value for File 1 is: ",
maxRevenue(projectOneFiles)
# print >> resultsFile, "The maximum value for File 2 is: ",
maxRevenue(projectTwoFiles)
# print >> resultsFile, "The maximum value for File 3 is: ",
maxRevenue(projectThreeFiles)
# print >> resultsFile, "The maximum value for File 4 is: ",
maxRevenue(projectFourFiles)
#
# resultsFile.close()
#
# print "Program Completed..."
# print "Check outputResults.txt file for results."
