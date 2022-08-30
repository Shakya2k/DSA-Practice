class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        cows=0
        d1=collections.Counter(secret)
        d2=collections.Counter(guess)
        for i in d1:
            if i in d2:
                cows+=min(d1[i],d2[i])
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls+=1
        return str(bulls) + "A" + str(cows-bulls) + 'B'
                
                
        