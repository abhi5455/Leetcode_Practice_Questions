class Solution(object):
    def majorityElement(self, nums):
        elementDict = {}
        for num in nums:
            if num in elementDict:
                elementDict[num] += 1
            else:
                elementDict[num] = 1

        largestCount = elementDict[nums[0]]
        majorityElement = nums[0]
        for key in elementDict:
            if elementDict[key] > largestCount:
                largestCount = elementDict[key]
                majorityElement = key

        return majorityElement
