class Solution(object):
    def isValid(self, s):
        parenthesesDict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in parenthesesDict:
                stack.append(char)
            elif not stack or char != parenthesesDict[stack.pop()]:
                return False
            else:
                pass

        return not stack

