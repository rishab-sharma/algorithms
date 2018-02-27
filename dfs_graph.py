from collections import defaultdict

class Graph:

	def __init__(self):

		self.graph = defaultdict(list)

	def addEdge(self , u , v):

		self.graph[u].append(v)

	def DFS(self, s ):

		visited = [False]*len(self.graph)

		self.DFS_recurser(s , visited)


	def DFS_recurser(self , s , visited):

		visited[s] = True
		print(s)

		for i in self.graph[s]:
			if visited[i] == False:
				visited[i] = True
				self.DFS_recurser(i , visited)

# Driver 
g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS(2)