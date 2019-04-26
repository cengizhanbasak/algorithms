# given a sorted array, find the index of number if exists
# return -1 if not exists
# O(logn) time where n is length of the array

def search(arr,num):
  k=0
  a=1
  b=1
  fib = [0,1]
  while(a<len(arr)):
    a=a+b
    a,b = b,a
    fib += [a]
    k+=1
  removed = 0
  while(k>0):
    current = arr[removed+fib[k-1]]
    if(current==num):
      return removed + fib[k-1]
    elif(current>num):
      k=k-1
    elif(current<num):
      removed += fib[k-1]+1
      k=k-2
  # if fibonacci not able to reach the number, linear search
  if(len(arr)>removed):
    for i in range(removed,len(arr)):
      if(arr[i]==num):
        return i
  return -1

arr = list(range(100))
for i in range(100):
  print(search(arr,i))
