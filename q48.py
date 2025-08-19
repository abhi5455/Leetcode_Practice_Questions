class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 or n == 0:
                return True
            else:
                return False
        count = 0
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                count += 1
            elif i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                count += 1
            elif flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
            if count >= n:
                return True
        return count >= n

