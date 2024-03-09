# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1,3,4,5]
# [1,1,2,4,5]
# [1,2,3,4,5]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n

def findDisappearedNumbers(nums: [int]) -> [int]:
    nums.sort() 
    temp = []
    result=[]
    i=0
    
    if len(nums)==2:
        if nums[0]!=1:
            result.append(1)
        elif nums[1]!=2:
            result.append(2)
        return result
    while i < len(nums):
        if nums[i]== i+1 or nums[i]==i+2:
            i=i+1
            
        else:
            result.append(i+1)
            i=i+1
        
    return result

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
            
   
        
        
    
        

