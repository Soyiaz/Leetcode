class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s) - 2):
            a = s[i]
            b = s[i + 1]
            c = s[i + 2]
            
            if a != b and a != c and b != c:
                count += 1

        return count
