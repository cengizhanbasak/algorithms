# problem: given an array, sort in increasing order
# O(nlogn) time and O(n) auxilary space
import random

# aim is to split the list into smaller sublists and merge them into a sorted list
# this is not an in-place sort, thus the sorted list is another object
# if we do like "arr = res", then arr reference changes, original array does not affected
# so i decided to copy res into arr one by one in the end
def sort(arr):
  res = mergesort(arr)
  for i in range(len(arr)):
    arr[i] = res[i]
  return arr

def mergesort(arr):
  if(len(arr) <= 1):
    return arr
  i = 0
  left = []
  while(i<len(arr)/2):
    left+=[arr[i]]
    i+=1
  right = []
  while(i<len(arr)):
    right+=[arr[i]]
    i+=1
  left = mergesort(left)
  right = mergesort(right)
  return merge(left,right)
  
# SEE: linear-merge
def merge(arr1,arr2):
  result = []
  p1 = 0
  p2 = 0
  while(p1<len(arr1) and p2<len(arr2)):
    if(arr1[p1]<arr2[p2]):
      result += [arr1[p1]]
      p1+=1
    else:
      result += [arr2[p2]]
      p2+=1
  while(p1<len(arr1)):
    result += [arr1[p1]]
    p1+=1
  while(p2<len(arr2)):
    result += [arr2[p2]]
    p2+=1
  return result

arr = list(range(1000))
random.shuffle(arr)

print(arr)
sort(arr) 
print(arr)
