class Solution(object):
    def sortedSquares(self, nums):
        return sorted(x * x for x in nums)

# Without sorting

# class Solution(object):
#     def sortedSquares(self, nums):
#         squares = []
#         i = 0
#         j = len(nums) - 1
#         while i <= j:
#             if nums[i]**2 > nums[j]**2:
#                 squares.append(nums[i]**2)
#                 i += 1
#             else:
#                 squares.append(nums[j]**2)
#                 j -= 1
#         return squares[::-1]
