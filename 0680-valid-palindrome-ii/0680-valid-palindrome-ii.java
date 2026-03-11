class Solution {
    public boolean validPalindrome(String s) {
        int first=0;
        int second=s.length()-1;
        
        while(first<second)
        {
            if(s.charAt(first) != s.charAt(second))
            {
                return isPalin(s,first+1,second) || isPalin(s,first,second-1);
            }
            first++;
            second--;
        }
        return true;
       
}

public boolean isPalin(String s,int first,int second)
{
while(first<second)
{
    if(s.charAt(first)!=s.charAt(second))
    {
        return false;
    }
    first++;
    second--;
}
return true;
}
}