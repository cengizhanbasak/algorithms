# depth first search is an algorithm on graph traversals
# starting from a root traversal is made by 
# going as deep as possible without backtracking
# implementation differs by how we represent the graphs

# example: directed, unweighted graph is represented by a 2D list (adjacency matrix)
# O(Vˆ2)
# note: this implementation does not traverse all the vertices

graph = [
  [0,1,0,0,0,0,0,0],
  [0,0,0,1,0,0,0,0],
  [0,1,0,0,0,0,0,0],
  [0,0,1,0,1,0,0,0],
  [0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1],
  [0,0,0,0,1,0,0,0],
  [0,0,0,0,0,0,1,0],
  ]


def dfs(graph,root,discovered):
  discovered += [root]
  print(root)
  adjacents = []
  for i in range(len(graph[root])):
    if(graph[root][i]==1):
      adjacents += [i]
  for i in adjacents:
    if(not i in discovered):
      dfs(graph,i,discovered)
  
discovered = []
dfs(graph,0,discovered)