class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        max_area = 0
        max_diagonal = 0
        for dimension in dimensions:
            diagonal_len = (dimension[0]**2 + dimension[1]**2)**0.5
            area = dimension[0] * dimension[1]
            if diagonal_len > max_diagonal or (diagonal_len == max_diagonal and area > max_area):
                max_diagonal = diagonal_len
                max_area = area
        return max_area