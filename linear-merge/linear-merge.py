# problem: merge two sorted lists(in increasing order)
# result array will be sorted
# total O(n+m) time where n and m are length of two arrays.

arr1 = [27, 47, 50, 52, 61, 81, 85, 91, 94, 95]
arr2 = [14, 22, 25, 38, 46, 51, 58, 61, 63, 64]


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

print(arr1)
print(arr2)
print(merge(arr1,arr2))
