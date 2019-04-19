# brute-first-search is a greedy approach to problems
# aim is to find a solution to various problems 
# by trying every possible output and checking if the output solves the problem
# not always the most efficient solution but guarantees to find a solution if exists
# SEE: linear-search

# example problem: find dividors of a number by exhaustively searching every number from 1 to the number
# O(n) time 

def dividors(num):
  res = []
  for i in range(1,num+1):
    if(num%i==0):
      res+=[i]
  return res

print(dividors(1200))