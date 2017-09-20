import re, sys

def main ():

    # --------- Importing all the files, numprojects, num weeks, and the data are included in the returnable --------- #

    testProject1 = importData('Qooqle_Projects_8_6_1477962811.78.txt')
    testProject2 = importData('Qooqle_Projects_10_30_1477962181.44.txt')
    testProject3 = importData('Qooqle_Projects_52_150_1477962917.86.txt')
    testProject4 = importData('Qooqle_Projects_500_1500_1477962966.94.txt')

    print("\nOutput will be sent to MaximumProfit.txt")

    output = open('MaximumProfit.txt', 'w')

    # ------------------------------ redirecting a print statement to the output file -------------------------------- #

    sys.stdout = output

    # ---------------------------------- Print statements and function calls ----------------------------------------- #
    print("CMPE 380 - ASSIGNMENT 4")
    print("KAL RADIKOV 10157529 || HENLEY CHIU 10141943")
    print("\n\nAnalysis for File 1 is below: ")
    revenueFind(testProject1)
    print("\n\nAnalysis for File 2 is below:")
    revenueFind(testProject2)
    print("\n\nAnalysis for File 3 is below:")
    revenueFind(testProject3)
    print("\n\nAnalysis for File 4 is below:")
    revenueFind(testProject4)


# ---------------------------------------- Maximum Income Function --------------------------------------------------- #

def revenueFind(dict):

    # ------------------- separating the data and extracting to their own variables ---------------------------------- #
    numWeeks = dict[0]
    numProjects = dict[1]
    projectDict = dict[2]
    profit = {}
    lastProject = {}

    # ------------ main loop that finds the maximum profit and last project to be  ----------------------------------- #

    for week in range(1, numWeeks+1):
        if week not in profit.keys():
            profit[week] = 0

    # ------------------------- checking to see if project can be assigned based on end time ------------------------- #

        for project in range(0, numProjects):
            if (projectDict[project]["start_week"] + projectDict[project]["duration"] - 1) <= week:
                if projectDict[project]["start_week"] == 1:
                    potentialProfit = projectDict[project]["value"]
                else:
                    potentialProfit = projectDict[project]["value"] + profit[projectDict[project]["start_week"] - 1]
                profit[week] = max(profit[week], potentialProfit)
                if profit[week] == potentialProfit:
                    lastProject[week] = project

    # ---------------------------------------- Assigning the max profit ---------------------------------------------- #

    maxProfit = profit[max(lastProject)]
    lastProject2 = lastProject[max(lastProject)]
    results = []

    print("The maximum income that can be generated is:", maxProfit)

    # ------------- Loop until revenue is 0 and a path is retraced from the last projects income --------------------- #

    while 1:
        results.append(lastProject2)
        maxProfit = maxProfit - projectDict[lastProject2]["value"]
        if (maxProfit == 0):
            break
        for weeks in profit:
            if profit[weeks] == maxProfit:
                week = weeks
        lastProject2 = lastProject[week]
    results.reverse()
    results[:] = [i+1 for i in results]

    # ----------------------- Prints out the path of projects that have the maximum income total --------------------- #

    print("The projects that must be complete are in this order:")

    for i in range(0, len(results)-1):
            print(results[i], "-> ", end="")
    print(results[len(results)-1])


# ----------------------------------------- Import Data Function ----------------------------------------------------- #

def importData(filename):

    data = []
    file = open(filename, 'r')

    # ------------------------------ read first 2 lines and collect data  -------------------------------------------- #

    contractWeeks = int(file.readline())
    numProjects = int(file.readline())

    # ---------------------- read file and put respective columns in the file in a dictionary ------------------------ #

    while True:
        y = file.readline()
        if y == '':
            break
        lineData = re.split('\t|\n', y)
        data.append({"project_num": int(lineData[0]), "start_week": int(lineData[1]), "duration": int(lineData[2]), "value": int(lineData[3])})
    file.close()

    return [contractWeeks, numProjects, data]

main()