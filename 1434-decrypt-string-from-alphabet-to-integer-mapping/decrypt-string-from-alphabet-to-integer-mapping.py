class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                result.append(chr(int(s[i:i+2]) + 96))  
                i += 3 
            else:
                result.append(chr(int(s[i]) + 96))  
                i += 1 
        
        return ''.join(result)
#Example 1
s = "10#11#12"
solution = Solution()
print(solution.freqAlphabets(s))  

#Example 2
s = "1326#"
solution = Solution()
print(solution.freqAlphabets(s)) 
