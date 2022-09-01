class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        c = Counter(words)
        c = sorted(c.items(), key=lambda x: (-x[1], x[0]))[:k]
        return [k for k, _ in c]
        