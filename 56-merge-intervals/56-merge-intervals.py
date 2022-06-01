class Solution:
    """def extend_array(self, intervals):
        output = []
        for i in intervals:
            i[1] += 1
            for j in range (i[0],i[1]):
                output.append(j)
        output.sort()
        return output
                
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        dummy = self.extend_array(intervals)
        #print (dummy)
        ans = []
        i=1
        while i < len(dummy):
            append = []
            append.append(dummy[i-1])
            j = i
            while (j<len(dummy)) and (dummy[j] - dummy[j-1] <= 1):
                j+=1
            append.append(dummy[j-1])
            i = j+1
            ans.append(append)
        return ans"""
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        j = 0
        if len(intervals) <= 1:
           return intervals
        else:
           j = 1
        result = []
        intervals = sorted(intervals, key=lambda x: x[0])
        start, end = intervals[0][0],intervals[0][1]
        while j<len(intervals):
           if end >= intervals[j][0]:
              if end < intervals[j][1]:
                 end = intervals[j][1]
              if start > intervals[j][0]:
                 start = intervals[j][0]
              if j == len(intervals)-1:
                 result.append([start,end])
              j+=1
           else:
              result.append([start,end])
              if j == len(intervals)-1:
                 result.append([intervals[j][0], intervals[j][1]])
              start, end = intervals[j][0], intervals[j][1]
              j+=1
        return result
                    
        
            
        