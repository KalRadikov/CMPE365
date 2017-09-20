# CISC/CMPE-365 Lab 2
# Robin Dawes

from random import *	# I will use methods from random to construct the graphs

class Graph (object):
	
	def __init__(self,vertices=20,type="Default"):
		self.n = vertices		# self.n is the number of vertices in G
		self.adj_lists = {}		# this dictionary will hold an adjacency list for each vertex
		self.degrees = {}		# this dictionary will hold the degree of each vertex
		self.m = 0			# self.m is the number of edges in G
			
		if type == "Tree":
			# build a tree - each new vertex is attached to ONE previously created vertex, selected at random
			print("\nBuilding a tree")
			self.adj_lists[1] = []
			for v in range(2,vertices+1):
				neighbour = randint(1,v-1)
				self.adj_lists[v] = [neighbour]
				self.adj_lists[neighbour].append(v)
			self.m = self.n - 1
		elif type == "Bipartite":
			# build a bipartite graph - each new vertex is added to either the "red" set or the "blue" set, then
			# joined to a randomly selected subset of the vertices in the other set.
			# You should convince yourself that the resulting graph is connected.
			print ("\nBuilding a bipartite graph")
			if self.n == 1:
				self.adj_lists[1] = []
			else:
				reds = [1]
				blues = [2]
				self.adj_lists = {1:[2],2:[1]}
				self.m = 1
				for v in range(3,vertices+1):
					if random() <= 0.5:
						# add the new vertex to the "reds"
						reds.append(v)
						# give it some "blue" neighbours
						e = randint(1,len(blues))
						neighbours = sample(blues,e)
						self.adj_lists[v] = neighbours
						for y in neighbours:
							self.adj_lists[y].append(v)
							self.m += 1
					else:
						# add it to the "blues"
						blues.append(v)
						# give it some "red" neighbours
						e = randint(1,len(reds))
						neighbours = sample(reds,e)
						self.adj_lists[v] = neighbours
						for y in neighbours:
							self.adj_lists[y].append(v)
							self.m += 1
		else:
			#  default - randomly create the edges
			print ("\nBuilding a completely random graph")
			self.adj_lists[1] = []
			already_coloured = {}		# this and other references to colouring in this block of code are
									# related to the "colour-while-building" process described in the lab
									# This process is not intended to find an optimal colouring, but only to
									# give a feasible colouring as a point of comparison for the "quick-colour" process
									
			already_coloured[1] = 1		# the value of already_coloured[x] is the colour that has been assigned to vertex x
			max_colour = 1
			for v in range(2,vertices+1):
				# give each vertex some neighbours among the vertices previously created
				e = randint(1,v-1)
				neighbours = sample(range(1,v),e)
				self.adj_lists[v] = neighbours
				n_colours = []
				# look at the colours used on the neighbours
				for y in neighbours:
					self.m += 1
					self.adj_lists[y].append(v)				# append v to y's list of neighbours
					n_colours.append(already_coloured[y])	# add y's colour to n_colours
				# choose a colour for the new vertex
				# in particular, choose the lowest numbered colour for v that is legal
				v_col = 1
				while v_col in n_colours:
					v_col += 1
				already_coloured[v] = v_col
				if v_col > max_colour:
					max_colour = v_col
			print ("\nColouring while building uses",max_colour,"colours")
		# compute degrees of the vertices - this is useful later when we need to sort the vertices by degree
		for v in self.adj_lists:
			self.degrees[v] = len(self.adj_lists[v])
		
					
	def show(self):
		# show the adjacency lists that define the graph
		for v in self.adj_lists:
			print (v, self.adj_lists[v])
			
	def try_2_colour(self):
		# attempt to 2-colour the graph
		q = [1]
		already_coloured = {}
		already_coloured[1] = 1		# colour vertex 1 with colour 1
		while len(q) != 0:
			x = q.pop(0)			# x has already been coloured, now we will colour its neighbours
			other_colour = 3 - already_coloured[x]		# other_colour is 1 or 2, depending on x's colour
			# examine x's neighbours
			for y in self.adj_lists[x]:
				if y not in already_coloured:
					already_coloured[y] = other_colour
					q.append(y)
				elif already_coloured[y] != other_colour:
					# one of x's neighbours already has the same colour as x.  Since all colours are forced, this is not fixable
					print ("ENNNNNNNGH!  G cannot be 2-coloured")
					return
		# we have run out of things to colour			
		if len(already_coloured) != self.n:
			print ("The graph is disconnected - try colouring each component individually")
		else:
			print ("2-colouring successful")
			for v in already_coloured:
				print (v, already_coloured[v])
	
	def merge_sort_vertices_descending(self):
		# returns a list of the vertices in descending degree order
		verts = range(1,self.n+1)
		if len(verts) > 1:
			return self.rec_merge_sort(verts)
		else:
			return verts
	
	def	rec_merge_sort(self,v):
		if len(v) <= 1:
			return v
		else:
			m = len(v)/2
			left = v[:m]
			right = v[m:]
			left_sorted = self.rec_merge_sort(left)
			right_sorted = self.rec_merge_sort(right)
			return self.merge(left_sorted, right_sorted)
			
	def merge(self,left,right):
		# this merge function is customized to sort into descending order
		l_max = len(left) - 1
		r_max = len(right) - 1
		l_current = 0
		r_current = 0
		combined = []
		while l_current <= l_max  and r_current <= r_max:
			if self.degrees[left[l_current]] >= self.degrees[right[r_current]]:	# compare the degrees of the vertices
																# and choose the larger 
				combined.append(left[l_current])
				l_current += 1
			else:
				combined.append(right[r_current])
				r_current += 1
		if l_current > l_max:
			combined.extend(right[r_current:])
		else:
			combined.extend(left[l_current:])
		return combined
			
	def quick_colour(self):
		# sort the vertices in decreasing degree order, then colour each one with the lowest available colour
		
		verts = self.merge_sort_vertices_descending()		
		
		# start colouring			
		already_coloured = {}
		max_colour = 0
		for v in verts:
			n_cols = []			# n_cols is the list of colours used on v's neighbours
			for y in self.adj_lists[v]:
				if y in already_coloured:
					n_cols.append(already_coloured[y])
			# now find the smallest colour that has not been used on any of v's neighbours		
			v_col = 1
			while v_col in n_cols:
				v_col += 1
			already_coloured[v] = v_col
			if v_col > max_colour:
				max_colour = v_col
			
		# print the results
		print )"\nQuick-colour used",max_colour,"colours")
		for v in self.adj_lists:
			print ("vertex ",v, "is coloured with ",already_coloured[v])
				
g1 = Graph(vertices = 30,type="Default")
#g1.show()
g1.quick_colour()
# Experiments show that quick_colour occasionally uses more colours than the colouring-while-building approach, which
# shows that quick_colour cannot always find an optimal colouring of the graph.