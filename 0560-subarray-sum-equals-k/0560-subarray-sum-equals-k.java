import java.util.*;
class Solution {
    public int subarraySum(int[] nums, int k) {
        Hashtable<Integer,Integer> h=new Hashtable<Integer,Integer>();
        int sum=0;
        int count=0;
        h.put(0,1);
        for(int i=0;i<nums.length;i++)
        {
          sum+=nums[i];
          if(h.containsKey(sum-k))
          {
         count += h.get(sum-k);
          }
        h.put(sum, h.getOrDefault(sum,0)+1);
        }

        return count;
        

    }
}