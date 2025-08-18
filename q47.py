class Solution(object):
    def reverseVowels(self, s):
        vowels = 'aeiouAEIOU'
        vowelIndices = []
        for i, char in enumerate(s):
            if char in vowels:
                vowelIndices.append(i)
        outStr = ""
        for i in range(len(s)):
            if i in vowelIndices:
                outStr += s[vowelIndices[len(vowelIndices) - vowelIndices.index(i)]]
            else:
                outStr += s[i]
        return outStr

