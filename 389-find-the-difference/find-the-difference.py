class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = 0
        # XOR all characters in both strings
        for char in s + t:
            result ^= ord(char)  # XOR the ASCII value of each character
        return chr(result)  # Convert the result back to a character

# Example 1
s1 = "abcd"
t1 = "abcde"
print(Solution().findTheDifference(s1, t1))  # Output: "e"

# Example 2
s2 = ""
t2 = "y"
print(Solution().findTheDifference(s2, t2))  # Output: "y"
