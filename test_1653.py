from pytest import mark

class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = count = 0
        for i in s:
            if i == 'b':
                count += 1
            elif count:
                count -= 1
                res += 1
        return res

@mark.parametrize('s,expected', [
    ('bbaaaaabbabb', 3)
])
def test_function(s, expected):
    output = Solution().minimumDeletions(s)
    assert output == expected