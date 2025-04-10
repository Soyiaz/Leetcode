class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    count += 1
            result.append(count)  
        return result

# Example 1:
nums1 = [8, 1, 2, 2, 3]
solution = Solution()
print(solution.smallerNumbersThanCurrent(nums1))

# Example 2:
nums2 = [6, 5, 4, 8]
print(solution.smallerNumbersThanCurrent(nums2)) 

# Example 3:
nums3 = [7, 7, 7, 7]
print(solution.smallerNumbersThanCurrent(nums3)) 
