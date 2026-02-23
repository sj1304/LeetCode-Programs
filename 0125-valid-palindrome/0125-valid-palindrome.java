class Solution {
    public boolean isPalindrome(String s) {
      s=s.replaceAll("[^a-zA-Z0-9]","");
      s=s.toLowerCase();
      System.out.println(s);
      boolean f=true;
      int i;
      for(i=0;i<s.length()/2;i++){
        if(s.charAt(i)!=s.charAt(s.length()-i-1))
           {f=false;
           break;}
      }
      return f;
    }
}