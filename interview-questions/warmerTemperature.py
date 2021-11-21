'''#1. Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

###
Input: temperatures = [73,74,75,71,69,72,76,73] [1,1,4,2,1,1,0,0]
Output: [1,1,4,2,1,1,0,0]
[40,10,31] [1,0,0,1,0]
storeLargest 
            


Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]

[73,74,75,71,69,72,76,73]

{73:0} []
74, pop 73 out res[map[T[i-1]]] = i - map[73] res[1-0] 

{74:1} , res[0] = 1

75, {75:2} , res = [1,1] 
71, {75:2, 71:3} , res = [1,1]
69, {75:2, 71:3, 69:4} , res = [1,1]
72, 
   {75,71} res [1,1,0,0,1]
   {75}  res [1,1,0,2,1]
  {75:2, 72:5} [1,1,0,2,1]
76, 
    {75} res [1,1,0,2,1,1]
    
    {} res [1,1,4,2,1,1]
    {76:6} [1,1,4,2,1,1]
73, 
    [1,1,4,2,1,1,0,0]
    '''
#temp
Input: temperatures = [30,40,50,35, 40] [0,0,0,0,0]
Output: [1,1,1,0]     35, [0,0,0,1,0]
        
[70,30,60,40]

cache = {temp[0]:0}                 {30:0}
res = [0 for i in range(len(temp))] [0,0,0,0]

for i in range(1,len(temp)):     

    if temp[i-1] >= temp[i]:
        cache[temp[i]] = i
        continue
    idx = i
    while cache and idx >= 0 and temp[idx-1] < temp[i]:
        res[idx-1] = i-idx+1     #[1,1,1,0]
        cache.pop(temp[idx-1])
        idx -= 1 
    cache[temp[i]] = i   #{60:3}
return res

