from pytest import mark

class Solution:
    def numTeams(self, rating: list[int]) -> int:
        total = 0
        for i, e in enumerate(rating):
            l = i - 1
            r = i + 1
            countl, countl1, countr, countr1 = 0, 0, 0, 0
            while l >= 0:
                if rating[l] < e:
                    countl += 1
                if rating[l] > e:
                    countl1 += 1
                l -= 1

            while r < len(rating):
                if rating[r] > e:
                    countr += 1
                if rating[r] < e:
                    countr1 += 1
                r += 1
            if countl != 0 and countr != 0:
                total += countl * countr
            if countl1 != 0 and countr1 != 0:
                total += countl1 * countr1 
                
        return total

        

@mark.parametrize(
    'rating,expected',
    [
        ([2,5,3,4,1], 3)
    ]
)
def test_function(rating, expected):
    output = Solution().numTeams(rating)
    assert output == expected

