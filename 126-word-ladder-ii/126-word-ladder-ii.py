from collections import defaultdict as dd

def reductions(w):
    """
	Simple helper function that maps each word to that word with one letter replaced by '.'
	
	Used to find neighbors in the graph
	"""
    for i in range(len(w)):
        yield w[:i] + "." + w[i+1:]


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        neighbors = dd(set)
        sets = dd(set)
		
		# beginWord can be safely added to the graph and this is helpful to handle edge cases later
        wordList = set(wordList) | set([beginWord])
		
		# First figure out the neighbors of each node. We do this by adding each word to a collection of words that differ
		# by one letter only
		
        for w in wordList:
            for x in reductions(w):
                sets[x].add(w)
        
        for w in wordList:
            for x in reductions(w):
                neighbors[w] |= sets[x]
               
		# We then run a BFS starting at the end to determine the distance of each node to the end
        distances = dd(lambda: float('inf'))
        distances[endWord] = 0
        search = [endWord]
        d = 0
        while search:
            next_search = []
            for s in search:
                for n in neighbors[s]:
                    if n in distances:
                        continue
                    distances[n] = d + 1
                    next_search.append(n)
            search = next_search
            d += 1
         
		# If we never reached beginWord in our DFS there are no solutions here, return an empty list
        if beginWord not in distances:
            return []
            
		# Our recursive function that explores the graph from the start decreasing the distance by one each time and yielding
		# all the paths
        def paths(start):
            if start == endWord:
                yield [start]
                return
            
            d = distances[start]
            for n in neighbors[start]:
                if distances[n] != d -1:
                    continue
                for p in paths(n):
                    yield [start] + p
        
        return paths(beginWord)