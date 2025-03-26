class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        total_sum = sum(salary) - min(salary) - max(salary)
        count = len(salary) - 2
        return total_sum / float(count)

# Example 1
salary = [4000, 3000, 1000, 2000]
solution = Solution()
print(solution.average(salary))  

# Example 2
salary = [1000, 2000, 3000]
print(solution.average(salary))  
