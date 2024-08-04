from pytest import mark

@mark.parametrize(
    'rowSum, colSum, expected_output',
    [
        ([3, 8], [4, 7], [[3, 0], [1, 7]]),
        ([5,7,10], [8,6,8], [[5, 0, 0], [3, 4, 0], [0, 2, 8]]),
    ]
)
def test_function(rowSum, colSum, expected_output):
    output = Solution().restoreMatrix(rowSum, colSum)
    print(output)
    assert output == expected_output
    
class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        output = [[0] * len(colSum) for _ in range(len(rowSum))]
        for i, row in enumerate(rowSum):
            for j, col in enumerate(colSum):
                output[i][j] = min(row, col)
                row -= output[i][j]
                colSum[j] -= output[i][j]
            rowSum[i] = row

        return output