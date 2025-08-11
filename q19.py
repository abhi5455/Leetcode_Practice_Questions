class Solution(object):
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans


# Another Solution

# class Solution(object):
#     def buildArray(self, nums):
#         ans = [0 for i in nums]
#         for i in range(len(nums)):
#             ans[i] = nums[nums[i]]
#         return ans