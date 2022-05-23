class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        def say(string):
            start = 0
            store = []
            if len(string) == 1:
                return (str(len(string))+string)
            else:
                for i in range (len(string)):
                    if i == 0:
                        continue
                    if string[i] != string[i-1]:
                        store.append(string[start:i])
                        start = i
                store.append(string[start:])
                if store == []:
                    return (str(len(string))+string[0])
                else:
                    s = ""
                    for i in range (len(store)):
                        s += (str(len(store[i]))+store[i][0])
                    return s
        return say(self.countAndSay(n-1))