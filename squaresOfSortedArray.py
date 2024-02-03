def sortedSquares( nums: [int]) -> [int]:
    start = 0
    end = len(nums)-1
    
    while start <= end:
        nums[start] = nums[start]*nums[start]
        if nums.count(nums[start]) >1:
            nums.remove(nums[start])
            end= end-1
            continue
        start = start+1
    nums.sort()       
    return nums

print(sortedSquares([-4,-1,0,1,4,5]))