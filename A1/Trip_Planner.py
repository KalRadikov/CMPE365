# CISC/CMPE-365 Lab 1
# Robin Dawes

from random import *		# methods from random will be used to create graphs

def best_route(G,A,B):
	# G is a dictionary where each item is a vertex and the associated dat is a list of tuples, each of the form (destination, departure time, arrival time)
	# A is the vertex we want to start at
	# B is the vertex we wish to reach
	
	# all times are hours offset from time 0
	T = {}	# time of earliest arrival dictionary
	for v in G:
		if v != A:
			T[v] = -1		# use -1 to indicate that we have not yet found a route to this vertex
	T[A] = 0
	P = {}	# predecessor dictionary  - when we finish, P[x] is x's immediate predecessor on the optimal route to x
	R = {}	# reached dictionary - R keeps track of the vertices we have reached
	R[A] = 1
	Q = [A]	# Q is a list of the vertices we have seen but not yet processed
	
	while len(Q) != 0:
		# let x be the vertex in Q with minimum T
		x = Q[0]
		for v in Q[1:]:
			if T[v] < T[x]:
				x = v
		# if x == B, break from loop because we have reached our destination
		if x == B:
			break
		else:
			print ("expanding from",x,", listing only flights that depart after time",T[x],"and are potentially useful")
			# for each unreached neighbour i of x


			for y,d,a in G[x]:  	# y is the neighbour, 
							# d is the departure time of the flight from x to y, 
							# a is the arrival time at y
				
				if y not in R:		# make sure y has not been reached already
					if d > T[x]:	# make sure the flight is possible (ie its departure time is not too early for us to catch it)
						print ("	flight to", y, "departs at",d, "and arrives at",a)
						if (T[y] == -1)  or (a < T[y]):	# flight is an improvement on previous best time to reach y
							T[y] = a
							P[y] = x
							if y not in Q:
								Q.append(y)
		Q.remove(x)
		R[x] = 1


		
	if x == B:
		Route = [B]
		x = B
		# build the route in reverse order using P[]
		while x != A:
			Route.append(P[x])
			x = P[x]
		Route.reverse()



		print ("\n\nOptimal route from",A,"to",B,':\n')
		for i in range(len(Route)-1):
			print ("Fly from",Route[i],"to",Route[i+1],"arriving at",T[Route[i+1]])
		print ("\nArrival time at destination: ",T[B])
	else:
		print ("\nThere is no valid path from",A,"to",B)
		
	
# simple test data set
'''network = {}
network[1] = [		(2,1,2),
				(2,3,6),
				(3,2,8),
				(4,4,8)
			]
network[2] = [		(3,7,9),
				(4,3,4)
			]
network[3] = [		(1,1,2),
				(2,2,4),
				(4,1,4),
				(4,7,8)
			]
network[4] = [		(1,1,3),
				(1,6,8),
				(2,2,4),
				(3,5,6)
			]
'''
network = {}
network[1] = [		(2,2,1)

			]
network[2] = [		(3,6,7),
				(3,8,9)
			]
network[3] = [		(1,8,10)

			]

best_route(network, 2,1)
 
 
 
 
 
 
 
 
 
