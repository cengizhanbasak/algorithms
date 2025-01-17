# depth first search is an algorithm on graph traversals
# starting from a root, traversal is made by 
# going as deep as possible without backtracking
# implementation differs by how we represent the graphs

# example: directed, unweighted graph is represented by a 2D list (adjacency matrix)
# O(Vˆ2)

graph1 = [
  [0,1,0,0,0,0,0,0],
  [0,0,0,1,0,0,0,0],
  [0,1,0,0,0,0,0,0],
  [0,0,1,0,1,0,0,0],
  [0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1],
  [0,0,0,0,1,0,0,0],
  [0,0,0,0,0,0,1,0]
  ]

graph2 = [
  [0,1,1,0,0,0,0,0],
  [0,0,1,1,0,0,0,0],
  [0,0,0,1,0,1,0,0],
  [0,0,0,0,1,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,1,0]
]


def dfs(graph,root,discovered):
  discovered += [root]
  print(root)
  for i in range(len(graph[root])):
    if(graph[root][i]==1):
      if(not i in discovered):
        dfs(graph,i,discovered)


dfs(graph1,0,[])

# second example: graph is represented by it's adjacency list
# O(V+E) (number of vertices + number of edges)

graph1_adjlist = [
  [1],
  [3],
  [1],
  [2,4],
  [5],
  [7],
  [4],
  [6]
]

graph2_adjlist = [
  [1,2],
  [2,3],
  [3,5],
  [4],
  [],
  [],
  [],
  [6]
]

def dfs2(adjlist,root,discovered):
  discovered += [root]
  print(root)
  for i in adjlist[root]:
    if(not i in discovered):
        dfs2(adjlist,i,discovered)

dfs2(graph1_adjlist,0,[])