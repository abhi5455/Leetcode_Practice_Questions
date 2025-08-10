class Solution(object):
    def isHappy(self, n):
        seen = []
        while n != 1:
            if n in seen:
                return False
            else:
                seen.append(n)
                n = sum(int(d) ** 2 for d in str(n))

        return True
