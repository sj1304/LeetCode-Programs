import java.util.*;
class Solution {
    public int majorityElement(int[] nums) {

        Hashtable<Integer, Integer> ht = new Hashtable<>();
        int max = 0;
        int element = 0;

        for (int i=0;i<nums.length;i++) {

            int count = ht.getOrDefault(nums[i], 0) + 1;
            ht.put(nums[i], count);

            if (count > max) {
                max = count;
                element = nums[i];
            }
        }

        return element;
    }
}