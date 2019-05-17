# Find shortest path between two nodes in a graph
# This algorithm finds all shortest paths from a root, creating a shortest path tree

graph = [
  [0,7,9,2147483647,2147483647,14],
  [7,0,10,15,2147483647,2147483647],
  [9,10,0,11,2147483647,2],
  [2147483647,15,11,0,6,2147483647],
  [2147483647,2147483647,2147483647,6,0,9],
  [14,2147483647,2,2147483647,9,0]
]

# Running time: O(nˆ2)
def djikstras(graph,root,target):
  shortestPaths = [2147483647]*len(graph)
  shortestPaths[root] = 0
  visited = []
  current = root
  while(len(visited)< len(graph)):
    visited+=[current]
    for i in range(len(graph)):
      if(i!=current and graph[current][i]+shortestPaths[current]<shortestPaths[i]):
        shortestPaths[i] = graph[current][i]+shortestPaths[current]
    currentMin = -1
    for i in range(len(shortestPaths)):
      # to find first non visited node
      if(i not in visited and currentMin == -1):
        currentMin = i
      if(i not in visited and shortestPaths[i] < shortestPaths[currentMin]):
        currentMin = i
    current = currentMin
  
  return shortestPaths[target]

print(djikstras(graph,0,0))
print(djikstras(graph,0,1))
print(djikstras(graph,0,2))
print(djikstras(graph,0,3))
print(djikstras(graph,0,4))
print(djikstras(graph,0,5))