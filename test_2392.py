from collections import defaultdict
from pytest import mark

class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        
        def dfs(source, adj, visit, path, order):
            if source in path:
                return False
            if source in visit:
                return True
            visit.add(source)
            path.add(source)
            for c in adj[source]:
                if not dfs(c, adj, visit, path, order):
                    return False
            path.remove(source)
            order.append(source)
            return True

            
            
        def topo_sort(edges):
            adj = defaultdict(list)
            for left, right in edges:
                adj[left].append(right)
                
            visit, path= set(), set()
            order = []
            for n in range(1, k+1):
                if not dfs(n, adj, visit, path, order):
                    return []
            return order[::-1]
            
        
        row_arr, col_arr = topo_sort(rowConditions), topo_sort(colConditions)
        if not row_arr or not col_arr:
            return []
        row_map = { r:i for i, r in enumerate(row_arr)}
        col_map = { c:i for i, c in enumerate(col_arr)}
        
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            matrix[row_map[num]][col_map[num]] = num
            
        return matrix
            


@mark.parametrize('k, rowConditions,colConditions,exptected', [
    (3, [[1,2],[3,2]],[[2,1],[3,2]],[[3,0,0],[0,0,1],[0,2,0]]),
    (3, [[1,2],[2,3],[3,1],[2,3]],[[2,1]], []),
])
def test_buildMatrix(k, rowConditions, colConditions, exptected):
    output = Solution().buildMatrix(k, rowConditions, colConditions)
    assert output == exptected