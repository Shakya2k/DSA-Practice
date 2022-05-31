class Solution:
    """def pascal_row(self, num: int) -> list:
        row = []
        for i in range (num):
            if i == 0:
                row.append(1)
            elif i == num-1:
                row.append(1)
            else:
                x = self.pascal_row(num-1)[i-1]
                y = self.pascal_row(num-1)[i]
                row.append(int(x+y))
        return row
                
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range (numRows):
            output.append(self.pascal_row(i+1))
        return output"""
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1: return [[1]]
    
        res = [[1],[1,1]]
    
        for i in range(2,numRows):
	
            lis = []
            temp = res[-1]
		
		    #START
            lis.append(temp[0])
            
            for j in range(1,len(temp)):
                lis.append(temp[j] + temp[j-1])
                
            lis.append(temp[-1])
            #END
            
            res.append(lis) 
    
        return res