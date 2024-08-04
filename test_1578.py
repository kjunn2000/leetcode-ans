from pytest import mark

class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        last_arr = []
        all_ele_arr = []
        for num in nums:
            temp_arr = []
            if last_arr:
                temp_arr = [a + num for a in last_arr]
            temp_arr.append(num)
            last_arr = temp_arr
            all_ele_arr.extend(temp_arr)

        all_ele_arr.sort()

        return sum(all_ele_arr[left-1:right]) % (pow(10,9) + 7)

        
@mark.parametrize('nums,n,left,right,expected', [
    ([1,2,3,4], 4, 1, 5, 13),
    ([1,2,3,4], 4, 3, 4, 6),
    ([1,2,3,4], 4, 1, 10, 50),
])
def test_function(nums,n,left,right,expected):
    ans = Solution().rangeSum(nums,n,left,right)
    assert ans == expected 
