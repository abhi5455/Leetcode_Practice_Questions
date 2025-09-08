class Solution(object):
    def getNoZeroIntegers(self, n):
        for i in range(1, n):
            if not self.has_zero(i) and not self.has_zero(n-i):
                return [i, n-i]

    def has_zero(self, num):
        return '0' in str(num) 