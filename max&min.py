def minmax(nums:[int])->[int]:
    min =nums[0]
    max=nums[0]
    for i in nums:
        if i< min:
            min =i
            
    for j in nums:
        if j>max:
            max=j
    return [min,max]
            
print(minmax([1,12,3,1,0]))