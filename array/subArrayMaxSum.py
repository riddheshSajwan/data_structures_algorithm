
def maxSubArray(nums):
    sum = 0
    maxSum = nums[0]
    
    for item in nums:
        sum += item
        maxSum = max([maxSum,sum])
        if sum < 0:
            sum =0
        else:
            continue
    return maxSum

maxSubArray([-2,1,-3,4,-1,2,1,-5,4])