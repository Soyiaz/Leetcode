class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Do not return anything, modify nums in-place instead.
        """
        non_zero_pos = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos] = nums[i]
                non_zero_pos += 1
        for i in range(non_zero_pos, len(nums)):
            nums[i] = 0

#Example 1
nums1 = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums1)
print(nums1)

#Example 2
nums2 = [0]
Solution().moveZeroes(nums2)
print(nums2)  


