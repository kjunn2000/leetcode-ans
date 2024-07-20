from queue import Queue

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacencyMap = {}
        for flight in flights:
            if flight[0] in adjacencyMap:
                adjacencyMap[flight[0]].append([flight[1], flight[2]])
            else:
                adjacencyMap[flight[0]] = [[flight[1], flight[2]]]
        dstCost = [math.inf] * n
        q = Queue()
        q.put((src, 0))
        stop = 0
        while not q.empty() and stop <= k:
            size = q.qsize()
            for _ in range(size):
                s, pathSum = q.get()

                if s not in adjacencyMap: continue

                for flight in adjacencyMap[s]:
                    if flight[1] + pathSum >= dstCost[flight[0]]: continue
                    dstCost[flight[0]] = flight[1] + pathSum
                    q.put((flight[0], dstCost[flight[0]]))

            stop += 1

        return dstCount[dst] if dstCount[dst] != math.inf else -1