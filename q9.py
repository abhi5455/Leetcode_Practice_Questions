class Solution(object):
    def twoSum(self, nums, target):
        inspected = {}
        for i, num in enumerate(nums):
            if (target - num) in inspected:
                return [inspected[target-num], i]
            else:
                inspected[num] = i
        return []


# Another solution - O(n²)

# class Solution(object):
#     def twoSum(self, nums, target):
#         soln = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if(nums[i]+nums[j] == target):
#                     soln.append(i)
#                     soln.append(j)
#         return soln