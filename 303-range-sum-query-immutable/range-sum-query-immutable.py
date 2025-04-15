class NumArray:

    def __init__(self, nums):
        self.nums = nums  

    def sumRange(self, left, right):
        total = 0  
        i = left
        while i <= right:  
            total += self.nums[i]  
            i += 1
        return total  