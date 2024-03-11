
# 349. Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# solution1

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p1,p2=0,0
        result = []
        nums1.sort()
        nums2.sort()
        while p1 <len(nums1) and p2 < len(nums2):
            if nums1[p1]== nums2[p2] and nums1[p1] not in result:
                result.append(nums1[p1])
                p1=p1+1
                p2=p2+1
            elif nums1[p1] in result or nums1[p1] < nums2[p2]  :
                p1=p1+1
            else :
                p2 = p2 +1
        return result
#solution2
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = set(nums1)
        y = set(nums2)
        return list(y-(y-x))
#solutionn 3
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))