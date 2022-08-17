class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        words_morse = []
        
        #first loop to traverse along 'words'
        for word in words:
            
            word_morse = ""
            
            for letter in word: #second loop to traverse along each word in 'words'
                
                tab = ord(letter) - ord('a') #getting index of letter using ASCII
                word_morse += morse[tab]
                
            words_morse.append(word_morse) #storing converted morse word
            
        words_morse = set(words_morse) #using set to store only unique values
        
        return len(words_morse) #returning length of the final set to get result
        
        