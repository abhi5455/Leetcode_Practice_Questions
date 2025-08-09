class Solution(object):
    def romanToInt(self, s):
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        number = 0

        for i in range(len(s)):
            if i + 1 < len(s) and symbols[s[i]] < symbols[s[i + 1]]:
                number -= symbols[s[i]]
            else:
                number += symbols[s[i]]

        return number


# Another solution

# class Solution(object):
#     def romanToInt(self, s):
#         symbols = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
#
#         number = 0
#         i = 0
#         while i < len(s):
#             if i + 1 < len(s) and symbols[s[i]] < symbols[s[i + 1]]:
#                 number += symbols[s[i + 1]] - symbols[s[i]]
#                 i += 2
#             else:
#                 number += symbols[s[i]]
#                 i += 1
#
#         return number