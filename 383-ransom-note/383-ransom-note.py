class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        visited = []
        for i in ransomNote:
            if i in magazine and (ransomNote.count(i)<=magazine.count(i)):
                c = magazine.index(i)
                visited.append(c)
        if len(visited)==len(ransomNote):
            return True
        else:
            return False
            