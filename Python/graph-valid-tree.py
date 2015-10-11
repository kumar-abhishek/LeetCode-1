# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)

# BFS solution.
class Solution:
    # @param {integer} n
    # @param {integer[][]} edges
    # @return {boolean}
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False

        visited_from, neighbors = 0, 1
        nodes = {}  # A dictionary to track each node's [visited_from, neighbors]
        for i in xrange(n):  # Space: O(|V|)
            nodes[i] = [-1, []]
        for edge in edges:   # Space: O(|E|)
            nodes[edge[0]][neighbors].append(edge[1])
            nodes[edge[1]][neighbors].append(edge[0])

        # BFS to check whether these edges make up a valid tree.
        visited = {}
        q = collections.deque()
        q.append(0)
        while q:
            i = q.popleft()
            visited[i] = True
            for n in nodes[i][neighbors]:
                if n != nodes[i][visited_from]:
                    if n in visited:
                        return False
                    else:
                        visited[n] = True
                        nodes[n][visited_from] = i
                        q.append(n)
        return True
