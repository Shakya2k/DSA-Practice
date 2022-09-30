class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events, sweepline, ans = [], [], []
        # We count the occurences of a specific height. Thus, we are able
        # to handle duplicate heights.
        heights = defaultdict(int)
        for start, end, height in buildings:
            # We sweep from left to right. If an insertion into the sweepline
            # happens at the same x-coordinate as the deletion of an element from
            # the sweepline, then the insertion operation is handled first.
            heappush(events, [start, False, height])
            heappush(events, [end, True, height])
        while events:
            x, delete, height = heappop(events)
            if not delete:
                if not sweepline or height > -sweepline[0]:
                    # Filter out collinear points, i.e., points that  share a 
                    # common x-coordinate along our skyline.
                    if ans and ans[-1][0] == x:
                        ans = ans[:-1]
                    ans.append([x, height])
                heights[height] += 1
                heappush(sweepline, -height)
            else:
                heights[height] -= 1
                if heights[height] == 0 and height == -sweepline[0]:
                    heappop(sweepline)
                    while sweepline and heights[-sweepline[0]] == 0:
                        heappop(sweepline)
                    ans.append([x, -sweepline[0] if sweepline else 0])
        return ans