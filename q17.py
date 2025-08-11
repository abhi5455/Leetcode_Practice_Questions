class Solution(object):
    def plusOne(self, digits):
        largeInteger = int(''.join(str(d) for d in digits))
        largeInteger += 1
        return [int(d) for d in str(largeInteger)]