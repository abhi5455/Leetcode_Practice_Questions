class Solution(object):
    def countKeyChanges(self, s):
        change = 0
        for i in range(1, len(s)):
            if s[i - 1].upper() != s[i].upper():
                change += 1
        return change

