from pytest import mark


@mark.parametrize(
    "names, heights, exptected",
    [
        (["Mary", "John", "Emma"], [180, 165, 170], ["Mary", "Emma", "John"]),
        (["Mary", "John", "Emma"], [180, 165, 170], ["Mary", "Emma", "John"]),
    ],
)
def test_sort_people(names: list[str], heights: list[int], exptected: list[str]):
    ans = Solution().sortPeople(names, heights)
    assert ans == exptected


class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        map_list = [(i, n, heights[i]) for i, n in enumerate(names)]
        output = sorted(map_list, key=lambda i: i[2], reverse=True)
        return [o[1] for o in output]
