# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
def missingNumber( nums: [int]) -> int:
    nums.sort()
    for i in range(len(nums)):
        if i != nums[i]:
           return i
        else:
            continue
    return len(nums)
        
print(missingNumber([3,0,1,4,5,6,7,8,9]))
        
        
 

