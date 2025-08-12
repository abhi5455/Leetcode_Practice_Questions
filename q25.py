class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        arr=[]
        for i in range(0, len(nums), 2):
            arr.append(nums[i+1])
            arr.append(nums[i])
        return arr


# Another Solution O(n²)

# class Solution(object):
#     def numberGame(self, nums):
#         arr=[]
#         for i in range(len(nums)/2):
#             x=nums.pop(nums.index(min(nums)))
#             y=nums.pop(nums.index(min(nums)))
#             arr.append(y)
#             arr.append(x)
#         return arr