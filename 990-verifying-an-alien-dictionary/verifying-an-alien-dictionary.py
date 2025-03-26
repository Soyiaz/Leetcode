class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_map = {char: i for i, char in enumerate(order)}
        
        def compare(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    return order_map[word1[i]] < order_map[word2[i]]
            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not compare(words[i], words[i + 1]):
                return False
        return True

# Example 1
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
sol = Solution()
print(sol.isAlienSorted(words, order))  

# Example 2
words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"
print(sol.isAlienSorted(words, order))  

# Example 3
words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(sol.isAlienSorted(words, order))  
