'''=============================================================================
 |   Assignment 1: Connecting Flights
 |
 |       Author:  Kal Radikov 10157529
 |				  Henley Chiu 10141943
 |
 |   Instructor:  Robin Dawes
 |
 |     Due Date:  Oct 5th 2016
 |
 +-----------------------------------------------------------------------------
 |
 |  Description:  Given a set of cities and flights between them, each flight with a departure time and arrival time,
 |	the program finds the route that starts in specified city A and ends in specified city B, and has the earliest
 |	possible arrival time in B. The flight plan may contain any number of flights but each flight in the route must have
 |	a departure time strictly greater than the arrival time of the previous flight in the route.
 |
 |        Input:  Takes a graph made up of a tuple of 4: Source City, Destination City,
 |				  Arrival Time, Departure Time
 |
 |       Output:  Produces the shortest know flight oath to the desination city
 |				  unless there is no flight path connecting them
 |
 |    Algorithm:  Dijkstra's Algorithm
 |
 *==========================================================================='''



import csv

flights = {}
with open('flights.txt') as flight_file: # importing the data and casting it as an int instead of a string
     next(flight_file)
     for row in csv.reader(flight_file, delimiter='\t'):
        if int(row[0]) not in flights:
           flights[int(row[0])] = [(int(row[1]), int(row[2]), int(row[3]))]
        else:
           flights[int(row[0])].append((int(row[1]), int(row[2]), int(row[3])))

def optimalRoute (G, A, B):

	T={} #B in the pseudocode
	R={} #used to hold reached cities
	P={} # used to hold the predecessors of the least weight path
	C=[A] # C is an array with the starting destination already in
	R[A] = True

	for v in G: # loop through all the keys in the graph and set destinations as weight -1 (infinity)
		if v != A:
			T[v]= -1
	T[A] = 0
	while C:
		x = C[0]
		for i in C[1:]: # looping through C to find the vertex x with minimmum Time (T)
			if T[i] < T[x]:
				x  = i
		if x == B:
			break
		else:
			for tuple in G[x]:
				if tuple[0] not in R: # check arrival city is not in Reached
					if T[x] < tuple[1]: # check if the min arrival time in city is feasible for next flight
						if T[tuple[0]] == -1 or tuple[2] < T[tuple[0]]:
							if tuple[0] not in C:
								C.append(tuple[0]) # add arrival city into seen cities
							T[tuple[0]] = tuple[2] # add arrival time of to Time dictionary
							P[tuple[0]] = x # adds min time vertex x to the list of predesessors
		R[x] = True
		C.remove(x)

	if x == B:
		best_route = [B]
		prev = B
		#print("P = ", P)
		while prev != A:
			best_route.append(P[prev])
			prev = P[prev] #build the route by reversing P
		best_route.reverse()
		print("Optimal route from city", A, "to city", B, "is:")
		print(best_route[0], end ="")
		for i in best_route[1:]:
			print(" to city", i, end = "")
		print("\nArrival time at destination is T =", T[B], "\n")
	else:
		print("There is no feasible path")

# using the non-trivial test data from the PDF
Graph = {}
Graph[1] = [		(2,1,2),	#destination, departure time, arrival time
				(2,3,6),
				(3,2,8),
				(4,4,8)
			]
Graph[2] = [		(3,7,9),
				(4,3,4)
			]
Graph[3] = [		(1,1,2),
				(2,2,4),
				(4,1,4),
				(4,7,8)
			]
Graph[4] = [		(1,1,3),
				(1,6,8),
				(2,2,4),
				(3,5,6)
			]

# Entering test inouts in the function

optimalRoute(flights, 50, 144)
optimalRoute(flights, 140, 92)
optimalRoute(flights, 99, 117)
optimalRoute(flights, 108, 28)
optimalRoute(flights, 192, 86)