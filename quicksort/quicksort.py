# problem: given an array, sort in increasing order
# O(nlogn) time
import random

def sort(arr):
  return qsort(arr,0,len(arr)-1)

def qsort(arr,low,high):
  if(low < high):
    p = partition(arr,low,high)
    qsort(arr,low,p-1)
    qsort(arr,p+1,high)
  return arr

def partition(arr,low,high):
  p = arr[high]
  i = low
  for j in range(low,high):
    if(arr[j] < p):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      i+=1
  temp = arr[i]
  arr[i] = arr[high]
  arr[high] = temp
  return i

arr = list(range(10000))
random.shuffle(arr)

print(arr)
sort(arr) 
print(arr)