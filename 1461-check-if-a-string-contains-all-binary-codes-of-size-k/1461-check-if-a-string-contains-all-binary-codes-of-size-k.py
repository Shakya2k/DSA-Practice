class Solution:
    """def generateBinary(self, num: int):
        output = []
        digits = ("0","1")
        n = 2
        self.returnBinary(digits, "", n, num, output)
        return output
    def returnBinary(self, array: set, prefix: str, length: int, klength: int, output: list):
        if klength == 0:
            output.append(prefix)
            return
        for i in range (length):
            newPrefix = prefix + array[i]
            self.returnBinary(array, newPrefix, length, klength-1, output)"""
        
    def hasAllCodes(self, s: str, k: int) -> bool:
        """output = self.generateBinary(k)
        for i in output:
            if i not in s:
                return False
        return True"""
        n=len(s)
        required_count=2 ** k        
        seen=set()
        for i in range(n-k+1):
            tmp=s[i:i+k]
            if tmp not in seen:
                seen.add(tmp)
                required_count-=1
                if required_count==0: # kill the loop once the condition is met
                    return True
        return False     