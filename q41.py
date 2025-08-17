class Solution(object):
    def subtractProductAndSum(self, n):
        nums = [int(x) for x in str(n)]
        product = 1
        for x in nums:
            product *= x
        return product - sum(nums)