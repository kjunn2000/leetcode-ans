class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        if len(nums) == 0: 
            return []
        positive, negative = 0, 0
        ans = []
        while len(ans) != len(nums):
            while nums[positive] < 0:
                positive += 1
            while nums[negative] > 0:
                negative += 1
            ans.append(nums[positive])
            ans.append(nums[negative])
            positive += 1
            negative += 1
        return ans