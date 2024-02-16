
class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        numberOfCount = defaultdict(int)

        for i in arr:
            numberOfCount[i] += 1

        sortedCount = sorted(numberOfCount.items(), key=lambda x: x[1])

        ans = 0
        for i in sortedCount:
            if i[1] > k:
                return len(sortedCount) - ans
            ans+=1
            k -= i[1]
        return 0
        