class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        romanNum = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = roman[::-1]
        romanNum = romanNum[::-1]
        
        rem = num
        answer = ""
        i = 0
        while rem > 0:
            #print (i)
            if rem < romanNum[i]:
                i += 1
                continue
            answer += roman[i]*(rem//romanNum[i])
            rem = rem%romanNum[i]
            #answer += roman[i]*(rem//romanNum[i])
            i += 1
        return answer
            
            