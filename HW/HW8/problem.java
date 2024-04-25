package HW.HW8;

public class problem {
        public int longestPalindrome(String s) {
            int[] charCounts = new int[128]; 
            for (char c : s.toCharArray()) {
                charCounts[c]++;
            }
            
            int length = 0;
            boolean hasOdd = false;
            for (int count : charCounts) {
                if (count % 2 == 0) {
                    length += count;  
                } else {
                    length += count - 1;  
                    hasOdd = true; 
                }
            }
            
            if (hasOdd) length += 1;  
            
            return length;
        
    }
    
    
}
