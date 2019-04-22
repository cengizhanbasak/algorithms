# breadth first search is an algorithm on graph traversals
# starting from a root, traversal is made by 
# visiting all the neighbours before going one level deeper
# implementation differs by how we represent the graphs

# example: directed, unweighted graph is represented by a 2D list (adjacency matrix)
# O(Vˆ2)

import queue

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

graph2 = [
  [0,1,1,0,0,0,0,0],
  [0,0,1,1,0,0,0,0],
  [0,0,0,1,0,1,0,0],
  [0,0,0,0,1,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,1,0],
]
  


def bfs(graph,root):
  discovered = []
  q = queue.Queue()
  q.put(root)
  discovered += [root]
  print(root)
  while(not q.empty()):
    v = q.get()
    for i in range(len(graph[v])):
      if(graph[v][i]==1):
        if(not i in discovered):
          discovered += [i]
          print(i)
          q.put(i)


# bfs(graph,0)


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

def bfs2(adjlist,root):
  discovered = []
  q = queue.Queue()
  q.put(root)
  discovered += [root]
  print(root)
  while(not q.empty()):
    v = q.get()
    for i in adjlist[v]:
      if(not i in discovered):
        discovered += [i]
        print(i)
        q.put(i)

bfs2(graph2_adjlist,0)
