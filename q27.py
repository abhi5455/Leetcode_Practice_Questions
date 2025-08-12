class Solution(object):
    def mostWordsFound(self, sentences):
        maxCount = 0
        for sentence in sentences:
            wordsCount = len(sentence.split(' '))
            if wordsCount > maxCount:
                maxCount = wordsCount
        return maxCount
