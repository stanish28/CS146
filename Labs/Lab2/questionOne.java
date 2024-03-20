package Lab2;
import java.util.Arrays;


public class questionOne {

    public static boolean isAnagram(String s, String t) {
       
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        
        
        Arrays.sort(sArray);
        Arrays.sort(tArray);
        
       
        return Arrays.equals(sArray, tArray);
    }

    public static void main(String[] args) {
        String s = "anagram";
        String t = "nagaram";
        System.out.println(isAnagram(s, t));  
        
        String s2 = "rat";
        String t2 = "car";
        System.out.println(isAnagram(s2, t2));
    }
    
}
