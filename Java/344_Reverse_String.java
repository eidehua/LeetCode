// Write a function that takes a string as input and returns the string reversed.
public class Solution {
    public String reverseString(String s) {
        char[] charArray = s.toCharArray();
        
        int startIndex = 0;
        int endIndex = charArray.length - 1;
        
        while(startIndex < endIndex) {
            char temp = charArray[startIndex];
            charArray[startIndex] = charArray[endIndex];
            charArray[endIndex] = temp;
            startIndex++;
            endIndex--;
        }
        
        return new String(charArray);
    }
}