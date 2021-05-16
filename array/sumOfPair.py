# sum = 8 
# arr = [1,4,3,7,0,6,-5]

comp = []

def sumOfPair(arr,sum):
  
 for i,item in enumerate(arr):
  if item in comp:
   return True
  if i == len(arr)-1:
   return False   
  else:
   comp.append(sum-item)

if sumOfPair([1,4,3,7,1,6,-5],0):
 print("pair found")
else:
 print("pair not found")