class Solution(object):
    def finalValueAfterOperations(self, operations):
        opDict = {'++X': 1, 'X++': 1, '--X': -1, 'X--': -1}
        x = 0
        for op in operations:
            x += opDict[op]
        return x
