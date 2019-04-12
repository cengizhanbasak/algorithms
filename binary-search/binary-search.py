# given a sorted array, find the index of number if exists
# return -1 if not exists
# O(logn) time where n is length of the array

def search(arr,num):
  l=0
  r=len(arr)
  while(l<r):
    if(num>arr[int((l+r)/2)]):
      l=int((l+r)/2)
    elif(num<arr[int((l+r)/2)]):
      r=int((l+r)/2)
    else:
      return int((l+r)/2)
  return -1
  

arr = list(range(100000))

print(search(arr,500))
