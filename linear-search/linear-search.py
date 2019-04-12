# given an array, find the index of number if exists
# return -1 if not exists
# O(n) time where n is length of the array
import random

def search(arr,num):
  i=0
  for n in arr:
    if(n==num):
      return i
    i+=1
  return -1

arr = list(range(100000))
random.shuffle(arr)

print(search(arr,1))
