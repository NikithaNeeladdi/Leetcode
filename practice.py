def test(nums:[])->[]:
    for i in nums:
        nums.remove(i)
    print(nums)
    return nums  
print(test([1,2,3,4,5,6])) 