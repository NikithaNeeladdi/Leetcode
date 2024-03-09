def maxFrequencyElements( nums: [int]) -> int:
        max_list=[]
        nums.sort() 
        
        for i in nums:
            temp = i
            counter = 1
            j=nums.index(i)+1
            
            while j < len(nums):
                if nums[j]==i:
                    counter = counter+1
                j= j+1
            max_list.append(counter)
            counter =0
            
            
            

        maximum_value = max(max_list)
        result = 0
        for i in max_list:
            if i== maximum_value:
                result = result +1
        return result      
    
print(maxFrequencyElements([1,2,2,3,1,4]))