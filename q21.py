class Solution(object):
    def getConcatenation(self, nums):
        ans = nums[:]
        for num in nums:
            ans.append(num)
        return ans
