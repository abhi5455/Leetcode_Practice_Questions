class Solution(object):
    def getConcatenation(self, nums):
        return nums + nums


# Another Solution

# class Solution(object):
#     def getConcatenation(self, nums):
#         ans = nums[:]
#         for i in range(len(nums)):
#             ans.append(nums[i])
#         return ans
