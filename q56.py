class Solution(object):
    def uniqueOccurrences(self, arr):
        occurence_dict = {}
        for x in arr:
            if x not in occurence_dict:
                occurence_dict[x] = 1
            else:
                occurence_dict[x] += 1
        occurence_arr = list(occurence_dict.values())
        return len(occurence_arr) == len(set(occurence_arr))