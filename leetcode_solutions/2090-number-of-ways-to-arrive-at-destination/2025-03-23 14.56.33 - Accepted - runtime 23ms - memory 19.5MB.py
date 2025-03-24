class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        # Step 1: Build the graph (adjacency list)
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))  # undirected

        # Step 2: Initialize distance and ways arrays
        dist = [float('inf')] * n
        dist[0] = 0

        ways = [0] * n
        ways[0] = 1

        # Step 3: Priority Queue for Dijkstra (min-heap)
        heap = [(0, 0)]  # (distance, node)

        while heap:
            curr_time, node = heapq.heappop(heap)

            if curr_time > dist[node]:
                continue  # Skip longer paths

            for neighbor, weight in graph[node]:
                time = curr_time + weight

                if time < dist[neighbor]:
                    # Found a shorter path to neighbor
                    dist[neighbor] = time
                    ways[neighbor] = ways[node]
                    heapq.heappush(heap, (time, neighbor))

                elif time == dist[neighbor]:
                    # Found another shortest path
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]