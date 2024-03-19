package HW.HW1;

public class questionOne {
    public static boolean isPalindrome(String s) {

        String cleaned = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        String str="";
        for(int i=cleaned.length()-1;i>-1;i--){
            str+=cleaned.charAt(i);
        }

        return cleaned.equals(str);
    }

    public static void main(String[] args) {
        String str = "A man, a plan, a canal: Panama";
        System.out.println(isPalindrome(str));  // true
        
        String s2 = "race a car";
        System.out.println(isPalindrome(s2)); // false
    }
    
}
