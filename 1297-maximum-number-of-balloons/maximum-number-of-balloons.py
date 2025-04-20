class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        from collections import Counter
        count = Counter(text)
        
        b = count['b'] if 'b' in count else 0
        a = count['a'] if 'a' in count else 0
        l = count['l'] // 2 if 'l' in count else 0
        o = count['o'] // 2 if 'o' in count else 0
        n = count['n'] if 'n' in count else 0
        result = b
        if a < result:
            result = a
        if l < result:
            result = l
        if o < result:
            result = o
        if n < result:
            result = n

        return result
