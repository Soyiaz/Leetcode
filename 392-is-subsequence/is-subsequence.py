class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pointer_s = 0
        for char in t:
            if pointer_s < len(s) and s[pointer_s] == char:
                pointer_s += 1
            if pointer_s == len(s):
                return True
        return pointer_s == len(s)


