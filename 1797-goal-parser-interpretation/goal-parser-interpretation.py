class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        return command.replace("()", "o").replace("(al)", "al")

#Example 1
sol = Solution()
print(sol.interpret("G()(al)")) 
#Example 2        
print(sol.interpret("G()()()()(al)"))  
#Example 3 
print(sol.interpret("(al)G(al)()()G")) 
