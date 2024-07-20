class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        m = left, n = right
        while m != n:
            m << 1
            n << 1
            count += 1
        ans = m
        ans >> 0 * count
        return ans