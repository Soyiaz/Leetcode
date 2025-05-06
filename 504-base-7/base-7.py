class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        result = []

        while num > 0:
            result.append(str(num % 7))
            num //= 7
        
        if negative:
            result.append('-')

        return ''.join(reversed(result))
