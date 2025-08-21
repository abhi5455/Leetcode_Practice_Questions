class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0, 0
        count = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                count += 1
                i += 1
            j += 1
        return count == len(s)

# Another Solution

# class Solution(object):
#     def isSubsequence(self, s, t):
#         t = list(t)
#         i = 0
#         j = 0
#         while True:
#             if j == len(s):
#                 return True
#             if i == len(t):
#                 return False
#             if t[i] != s[j]:
#                 t.remove(t[i])
#             else:
#                 i, j = i+1, j+1
#         return False
