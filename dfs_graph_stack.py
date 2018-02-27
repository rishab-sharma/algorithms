from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self , u , v):
		self.graph[u].append(v)

	def DFS(self , s):

		visited = [False]*len(self.graph)

		stack = []

		stack.append(s)

		while stack:

			s = stack.pop()

			visited[s] = True

			print(s)

			for i in self.graph[s]:
				if visited[i] == False:
					stack.append(i)

# Driver 
g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS(2)

