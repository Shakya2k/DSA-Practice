class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_to_list = s.split()
        str_to_list = str_to_list[::-1]
        
        res = ""
        
        for i in range (len(str_to_list)):
            
            if i != len(str_to_list) - 1:
                res += str_to_list[i] + " "
                
            else:
                res += str_to_list[i]
            
        return res
        