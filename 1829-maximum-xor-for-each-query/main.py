class Solution:
    def getMaximumXor(self, nums: list[int], maximum_bit: int) -> list[int]:
        n = len(nums)
        answer = [0] * n
        max_k = 2**maximum_bit - 1
        last_xor = nums[0]
        answer[-1] = last_xor ^ max_k
        for i in range(1, n):
            last_xor ^= nums[i]
            answer[n - i - 1] = last_xor ^ max_k

        return answer
