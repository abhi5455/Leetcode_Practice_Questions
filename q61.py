class Solution(object):
    def pivotArray(self, nums, pivot):
        lt = []
        gt = []
        eq = []
        for x in nums:
            if x < pivot:
                lt.append(x)
            elif x > pivot:
                gt.append(x)
            else:
                eq.append(x)
        return lt + eq + gt
