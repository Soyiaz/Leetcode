class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1] 
                if not prefix:  
                    return ""
        
        return prefix

# Example 1
strs = ["flower", "flow", "flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))  

# Example 2
strs = ["dog", "racecar", "car"]
print(solution.longestCommonPrefix(strs))  
