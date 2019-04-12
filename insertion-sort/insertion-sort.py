# problem: given an array, sort in increasing order
# O(n^2) time
import random

# algorithm depends on a wall
# where left of the wall is kept sorted
# items on the right are inserted to left
# until no item left on the right side of the wall
def sort(arr):
  wall = 1
  while(wall<len(arr)):
    i=wall
    while(i>0 and arr[i]<arr[i-1]):
      # XOR_SWAP
      arr[i] = arr[i]^arr[i-1]
      arr[i-1] = arr[i]^arr[i-1]
      arr[i] = arr[i]^arr[i-1]
      i-=1
    wall+=1

arr = list(range(100))
random.shuffle(arr)

print(arr)
sort(arr) 
print(arr)