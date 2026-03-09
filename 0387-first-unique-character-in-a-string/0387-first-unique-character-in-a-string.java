import java.util.*;
class Solution {
    public int firstUniqChar(String s) {
       Hashtable<Character,Integer> h=new Hashtable<>();
       int cnt=0;
       for(int i=0;i<s.length();i++)
       {
        if(!h.containsKey(s.charAt(i)))
        {
            h.put(s.charAt(i),1);
        }
        else
        {
            cnt=h.get(s.charAt(i));
            h.put(s.charAt(i),cnt+1);
        }
       }

       for(int i=0;i<s.length();i++)
       {
    if(h.get(s.charAt(i))==1)
    {
        return i;
    }
       }
       

       return -1;

    }
}