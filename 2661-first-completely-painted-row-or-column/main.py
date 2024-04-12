from collections import Counter
from itertools import chain


class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        row_len = len(mat[0])
        search_dict = dict()
        for i, num in enumerate(chain.from_iterable(mat)):
            search_dict[num] = self.get_x_y_from_index(i, row_len)

        counter = Counter()
        for i, num in enumerate(arr):
            x, y = search_dict[num]
            row_key, column_key = f"row{y}", f"column{x}"
            counter[row_key] += 1
            counter[column_key] += 1
            if counter[row_key] == row_len or counter[column_key] == row_len:
                return i

    def get_x_y_from_index(self, index, row_len):
        y, x = divmod(index, row_len)
        return x, y
