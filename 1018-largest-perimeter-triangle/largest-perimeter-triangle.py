class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        for i in range(len(nums) - 1, 1, -1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]
        return 0
# Example 1
nums = [2, 1, 2]
solution = Solution()
print(solution.largestPerimeter(nums))  

# Example 2
nums = [1, 2, 1, 10]
print(solution.largestPerimeter(nums)) 
