# problem: given an array, sort in increasing order
# O(n^2) time
import random

# algorithm depends on a wall
# where left of the wall is kept sorted
# items on the right are inserted to left
# until no item left on the right side of the wall
def sort(arr):
  wall = 0
  while(wall<len(arr)):
    i=wall
    minimum=i
    while(i<len(arr)):
      if(arr[i]<arr[minimum]):
        minimum = i
      i+=1
    temp = arr[wall]
    arr[wall] = arr[minimum]
    arr[minimum] = temp
    wall+=1

arr = list(range(100))
random.shuffle(arr)

print(arr)
sort(arr) 
print(arr)