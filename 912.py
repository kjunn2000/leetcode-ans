class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def divide(nums: list[int]):
            print(nums)
            if not nums or len(nums) < 2:
                return nums
            mid = len(nums) // 2
            left = divide(nums[:mid]) 
            right = divide(nums[mid:]) 
            return merge(left, right)

        def merge(left: list[int], right: list[int]) -> list[int]:
            if not left and not right:
                return []
            elif not left:
                return right
            elif not right:
                return left 
            ans = []
            l = r = 0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    ans.append(left[l]) 
                    l += 1
                else:
                    ans.append(right[r])
                    r += 1
                    
            if r < len(right):
                ans.extend(right[r:])
            elif l < len(left):
                ans.extend(left[l:])
            return ans

        return divide(nums)
    
print(Solution().sortArray([1, 3, 5, 15, 115]))