class Solution(object):
    def judgeCircle(self, moves):
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

# Another Solution

# class Solution(object):
#     def judgeCircle(self, moves):
#         coordinate = [0, 0]
#         for move in moves:
#             if move == 'R':
#                 coordinate[1] += 1
#             elif move == 'U':
#                 coordinate[0] += 1
#             elif move == 'L':
#                 coordinate[1] -= 1
#             else:
#                 coordinate[0] -= 1
#         return coordinate[0] == 0 and coordinate[1] == 0
