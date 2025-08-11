class Solution(object):
    def addDigits(self, num):
        digit = str(num)
        while len(digit) > 1:
            digit = str(sum(int(d) for d in digit))
        return int(digit)
