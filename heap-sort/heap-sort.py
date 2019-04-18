# problem: given an array, sort in increasing order
# O(nlogn) time
import random

# aim is to create a heap out of the given array and popping elements from the heap to get a sorted list
# first create a heap
# then pop elements from the heap until heap is empty
def sort(arr):
  hp = heapify(arr)
  i=0
  while(len(hp)>0):
    arr[i] = extract_min(hp) 
    i+=1
  return arr

def heapify(arr):
  res = []
  for num in arr:
    res+=[num]
    p = len(res)-1
    while(p>0 and res[p]<res[int(p/2)]):
      res[p],res[int(p/2)] = res[int(p/2)],res[p]
      p=int(p/2)
  return res


def extract_min(hp):
  min_element = hp[0]
  hp[0],hp[len(hp)-1] = hp[len(hp)-1],hp[0]
  hp.pop()
  p=0
  while((p*2+1 < len(hp))):
    minindex = p*2+1
    if(len(hp) > p*2+2 and hp[p*2+1]>hp[p*2+2]):
      minindex = p*2+2
    if(hp[p] > hp[minindex]):
      hp[p],hp[minindex] = hp[minindex],hp[p]
      p=minindex
    else:
      break
  return min_element


# to test if the heap is created correctly
def test_heapify(hp):
  i=0
  while(i<len(hp)/2):
    if(hp[i]>hp[i*2+1] and hp[i]>hp[i*2+2]):
      print("WRONG",i,hp[i])
      return
    i+=1
  print("PASS")



arr = list(range(100000))
random.shuffle(arr)


print(arr)
sort(arr) 
print(arr)
