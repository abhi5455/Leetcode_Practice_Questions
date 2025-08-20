class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [0] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

# Another Solutin

# class Solution(object):
#     def productExceptSelf(self, nums):
#         product = 1
#         for num in nums:
#             if num != 0:
#                 product*=num
#         res = []
#         if product == 1 and 1 not in nums:
#             return [0 for x in nums]
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 res.append(product) if nums.count(0) == 1 else res.append(0)
#             elif 0 in nums:
#                 res.append(0)
#             else:
#                 res.append(product//nums[i])
#         return res
