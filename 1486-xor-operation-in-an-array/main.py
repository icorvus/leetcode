from functools import reduce
import operator


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = (start + 2 * i for i in range(n))
        return reduce(operator.xor, nums)
