class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        """
        1 sec per edge
        starting at vertex 0, min seconds to collect all apples and come back to start

        BFS on undirected graph gives you shortest
        
        if dead end found where vertex has no neighbors ignore adding 2*pathsum

        apple 2
apple 2
VISIT set()
Current node 2
Path distance 0
VISIT set()
Current node 0
Path distance 2
VISIT set()
Current node 3
Path distance 2
VISIT set()
Current node 6
Path distance 2
ANS 2
apple 4
VISIT set()
Current node 4
Path distance 0
VISIT set()
Current node 1
Path distance 2
VISIT set()
Current node 0
Path distance 4
VISIT set()
Current node 5
Path distance 4
ANS 4
apple 5
VISIT set()
Current node 5
Path distance 0
VISIT set()
Current node 1
Path distance 2
VISIT set()
Current node 0
Path distance 4
VISIT set()
Current node 4
Path distance 4
ANS 4
        """
        def bfs(start):
            res = 0
            d = deque([(start, 0, set())])

            while d:
                current_node, path_sum, path_visit = d.popleft()
                path_visit = path_visit.copy() # deep copy

                if current_node == 0 or current_node in visited:
                    res += path_sum
                    visited.update(path_visit)
                    continue
                
                path_visit.add(current_node)

                for neighbor in graph[current_node]:
                    if neighbor not in path_visit:
                        d.append((neighbor, path_sum+2, path_visit))
            return res

        sol=0
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        apples = []
        
        

        for node in range(len(hasApple)):
            if hasApple[node] == True:
                apples.append(node)
        for apple in apples:
            if apple not in visited:
                ans = bfs(apple)
                sol += ans
        return sol