class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        charCounts = Counter(s)  
        
        length = 0
        hasOdd = False
        for count in charCounts.values():
            if count % 2 == 0:
                length += count 
            else:
                length += count - 1 
                hasOdd = True  
                
        if hasOdd:
            length += 1  
            
        return length
