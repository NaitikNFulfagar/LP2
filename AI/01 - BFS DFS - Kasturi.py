class Graph:
    def __init__(self):
        self.graph={}

    def add_edge(self,u,v):
        self.graph.setdefault(u,[]).append(v)
        self.graph.setdefault(v,[]).append(u)

    def dfs_util(self , vertex , visited):
        visited.add(vertex)
        print(vertex,end=" ")

        for neighbor in self.graph.get(vertex,[]):
            if neighbor not in visited :
                self.dfs_util(neighbor , visited)

    def dfs(self,start):
        visited = set()
        self.dfs_util(start , visited)

    def bfs(self,start):

        v = set()
        queue = [start]

        while queue:
            vertex = queue.pop(0)
            if vertex not in v :
                print(vertex,end=" ")
                v.add(vertex)

                for neighbor in self.graph.get(vertex,[]):
                    if neighbor not in v:
                        queue.append(neighbor)

g = Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(4,0)

print("Depth_First Search(DFS): ")
g.dfs(0)
print("\nBreadth-First search(BFS): ")
g.bfs(0)