class Solution(object):
    def countDigits(self, num):
        divDigits = [int(d) for d in str(num) if num % int(d) == 0]
        return len(divDigits)
