class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:

        if len(nums) < 3:
            return -1

        sorted_nums = sorted(nums)

        total_sum = sum(nums)

        ans = 0

        for i in range(len(sorted_nums) -1 , 1, -1):
            total_sum -= sorted_nums[i]
            if total_sum > sorted_nums[i]:
                return total_sum + sorted_nums[i]

        return -1