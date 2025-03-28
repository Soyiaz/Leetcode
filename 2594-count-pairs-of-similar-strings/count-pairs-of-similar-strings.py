class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def normalize(word):
            return ''.join(sorted(set(word)))

        normalized_words = [normalize(word) for word in words]
        count = 0
        n = len(words)
        
        for i in range(n):
            for j in range(i + 1, n):
                if normalized_words[i] == normalized_words[j]:
                    count += 1
        
        return count

#Example 1
words = ["aba", "aabb", "abcd", "bac", "aabc"]
solution = Solution()
print(solution.similarPairs(words))  

#Example 2
words = ["aabb", "ab", "ba"]
solution = Solution()
print(solution.similarPairs(words))  

#Example 3
words = ["nba", "cba", "dba"]
solution = Solution()
print(solution.similarPairs(words))  
