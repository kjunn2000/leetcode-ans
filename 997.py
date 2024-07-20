class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)
        for t in trust :
            in_degree[t[0]] += 1
            out_degree[t[1]] += 1
        for i in range (1, n+1):
            if in_degree[i] == 0 and out_degree[i] == n-1:
                return i     
        return -1