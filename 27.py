def removeElement(nums:[int], val: int) -> int:
        start = 0
        end = len(nums)-1
        counter = 0
        
        if len(nums)==2:
            if nums[0]==val:
                if nums[1]==val:
                    return 0
                nums.remove(nums[0])
                return 1
            if nums[1]==val:
                nums.remove(nums[1])
                return 1
                    
           
                
        
        while start <= end :
            if nums[start] == val:
                nums.remove(nums[start])
                nums.append('_')
                counter = counter+1
                continue
            start = start+1
            
        return len(nums)-counter
print(removeElement([2,2,3,3],3))