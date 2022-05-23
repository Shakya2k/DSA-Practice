class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ['' for _ in range (numRows)]
        indexes = [i for i in range (numRows)] + [i for i in reversed(range(1,numRows-1))]
        
        repeat = int((len(s) / (len(indexes))) + 1)
        indexes = indexes * repeat
        
        for index, ch in zip(indexes, s):
            rows[index] += ch
        
        return ''.join(rows)
        #return rows
            
                