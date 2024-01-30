def sortedSquares(nums: [int]) -> [int]:
    start =0
    end = len(nums)-1
    for i in range(len(nums)):
        nums[i]=nums[i]*nums[i]
    nums.sort()
    # for i in range(len(nums)-1):
    #     for j in range(i+1,len(nums)-1):
    #         if nums[i]>nums[i+1]:
    #             temp=nums[i]
    #             nums[i]=nums[i+i]
    #             nums[i+1]=temp
    return nums

print(sortedSquares([-4,-1,0,3,1]))
         
     