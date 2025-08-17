class Solution(object):
    def arraySign(self, nums):
        product = 1
        for x in nums:
            product *= x
        return self.signFunc(product)

    def signFunc(self, product):
        if product > 0:
            return 1
        elif product < 0:
            return -1
        return 0
