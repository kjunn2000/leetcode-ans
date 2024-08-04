from collections import defaultdict
import heapq
from pytest import mark


class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:

        adj_map = defaultdict(list)
        for (source, target, weight) in edges:
            adj_map[source].append((target, weight))
            adj_map[target].append((source, weight))

        def dijkstra(source) -> int:
            heap = [(0, source)]
            visit = set()

            while heap:
                dist, node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                    
                for (nei, dest2) in adj_map[node]:
                    nei_dest = dist + dest2
                    if nei_dest <= distanceThreshold:
                        heapq.heappush(heap, (nei_dest, nei))
            return len(visit) - 1

        city, min_count = -1, n
        for s in range(n):
            cities = dijkstra(s)
            if cities <= min_count:
                city, min_count= s, cities
            
        return city 


@mark.parametrize('n, edges, distanceThreshold, expected', 
                  [
                      (4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4, 3),
                      (5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2, 0),
                      (6, [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]], 20, 5)
                 ])
def test_function(n, edges, distanceThreshold, expected):
    output = Solution().findTheCity(n, edges, distanceThreshold)         
    assert output == expected