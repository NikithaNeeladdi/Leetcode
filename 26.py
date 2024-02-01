def removeDuplicates(nums:[int]) -> int:
    start = 0
    end = len(nums)-1
    counter = 0
    while start < end:
        if nums[start]== nums[start+1]:
            nums.remove(nums[start])
            counter= counter+1
            nums.append('_'+str(counter))
            
        else:
            start = start+1
            
    return len(nums)-counter
        
     
     
     
print(removeDuplicates([1,2,2,3,4,4]))