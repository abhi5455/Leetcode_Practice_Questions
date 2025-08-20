class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= maxCandies)
        return result
