from typing import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        # counter map
        sorted_count = sorted(Counter(word).items(), key=lambda a: -a[1])

        # loop 8 and record count (position * count)
        ans = 0
        layer = 1
        count = 0
        while sorted_count :
            ans += sorted_count.pop(0)[1] * layer
            count += 1
            if count == 8:
                count, layer = 0, layer + 1
        return ans

print(Solution().minimumPushes('aabbccddeeffgghhiiiiii'))