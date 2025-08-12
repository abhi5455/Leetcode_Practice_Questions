class Solution(object):
    def checkIfPangram(self, sentence):
        return len(set(sentence)) == 26

# Another Solution

# class Solution(object):
#     def checkIfPangram(self, sentence):
#         alphabets = 'abcdefghijklmnopqrstuvwxyz'
#         for char in alphabets:
#             if char not in sentence:
#                 return False
#         return True