class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
        
        return ''.join(merged)

# Example 1
word1 = "abc"
word2 = "pqr"
sol = Solution()
print(sol.mergeAlternately(word1, word2))  

# Example 2
word1 = "ab"
word2 = "pqrs"
print(sol.mergeAlternately(word1, word2))  

# Example 3
word1 = "abcd"
word2 = "pq"
print(sol.mergeAlternately(word1, word2))  
