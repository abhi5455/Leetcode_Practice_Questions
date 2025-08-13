class Solution(object):
    def xorOperation(self, n, start):
        nums = [start + 2 * i for i in range(n)]
        bitOR = 0
        for num in nums:
            bitOR = bitOR ^ num
        return bitOR
