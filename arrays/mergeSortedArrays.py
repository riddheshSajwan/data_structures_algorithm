# [1,4,6,10,12] [2,3,8,11,15]

def mergeSortedArrays(arr1, arr2):
 i = 0
 j = 0
 finalArray = []
 #print(arr1[5:])
 while i < len(arr1) and j < len(arr2):
  if (arr1[i] <= arr2[j]):
   #print(arr1[i])
   finalArray.append(arr1[i])
   i+=1
  else:
   #print(arr2[j])
   finalArray.append(arr2[j])
   j+=1
  
 print(i)
 if i == len(arr1):
  print("enter 1")
  finalArray += arr2[j:]
 elif j == len(arr2):
  finalArray += arr1[i:]
 return finalArray

print(mergeSortedArrays([1,4,6,10,12],[]))