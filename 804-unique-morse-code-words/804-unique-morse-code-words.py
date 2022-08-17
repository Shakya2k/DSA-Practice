class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        words_morse = []
        for word in words:
            word_morse = ""
            for letter in word:
                tab = ord(letter) - 97
                word_morse += morse[tab]
            words_morse.append(word_morse)
        words_morse = set(words_morse)
        return len(words_morse)
        
        