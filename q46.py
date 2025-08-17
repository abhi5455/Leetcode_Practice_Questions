class Solution(object):
    def canAliceWin(self, nums):
        singleSum = 0
        doubleSum = 0
        for num in nums:
            if len(str(num)) == 1:
                singleSum += num
            else:
                doubleSum += num
        return singleSum != doubleSum

# Another Solution

# class Solution(object):
#     def canAliceWin(self, nums):
#         singleSum = sum([x for x in nums if len(str(x)) == 1])
#         doubleSum = sum([x for x in nums if len(str(x)) == 2])
#         totalSum = sum(nums)
#         if (totalSum-singleSum < singleSum) or (totalSum-doubleSum < doubleSum):
#             return True
#         return False
