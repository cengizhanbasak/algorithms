# problem: given an array, sort in increasing order
# O(n^2) time
import random

def sort(arr):
  i = 0
  while(i<len(arr)):
    j=i+1
    while(j<len(arr)):
      if(arr[i]>arr[j]):
        # XOR_SWAP
        arr[i]= arr[i]^arr[j]
        arr[j]= arr[i]^arr[j]
        arr[i]= arr[i]^arr[j]
      j+=1
    i+=1
  return arr

arr = list(range(100))
random.shuffle(arr)

print(arr)
sort(arr) 
print(arr)