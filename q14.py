class Solution(object):
    def convertToTitle(self, columnNumber):
        excelIndex = ''
        while columnNumber > 0:
            columnNumber -= 1
            excelIndex = chr((columnNumber % 26) + ord("A")) + excelIndex
            columnNumber = columnNumber // 26
        return excelIndex
