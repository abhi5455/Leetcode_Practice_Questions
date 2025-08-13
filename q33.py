class Solution(object):
    def differenceOfSums(self, n, m):
        num1, num2 = 0, 0
        for x in range(1, n + 1):
            if x % m != 0:
                num1 += x
            else:
                num2 += x
        return num1 - num2
