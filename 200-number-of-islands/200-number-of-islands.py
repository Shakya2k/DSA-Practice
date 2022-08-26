class Solution:
    def numIslands(self, g: List[List[str]]) -> int:
        if not g:
            return 0
        
        rows, cols = len(g), len(g[0])
        vs = set()
        ans = 0
        
        def bfs(r, c):
            q = collections.deque()
            vs.add((r,c))
            q.append((r,c))
            
            while q:
                row, col = q.popleft()
                d = [[1,0],[-1,0],[0,1],[0,-1]]
                
                for dr, dc in d:
                    r, c = row + dr, col + dc
                    if ( r in range(rows) and 
                         c in range(cols) and
                         g[r][c] == "1" and
                         (r,c) not in vs):
                        q.append((r,c))
                        vs.add((r,c))
                        
        for r in range(rows):
            for c in range(cols):
                if g[r][c] == "1" and (r,c) not in vs:
                    bfs(r,c)
                    ans += 1
        
        return ans
                    