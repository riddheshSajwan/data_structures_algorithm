
def moveZeroes(nums):        
    for i in range(nums.count(0)):
        nums.append(nums.pop(nums.index(0)))
    print(nums)      

moveZeroes([1,0,-3,5,3,2,0,6,7])      