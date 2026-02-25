class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length == 0)
            return 0;

        int n = nums.length;

        int[] dp = new int[n];      // max product ending at i
        int[] minDp = new int[n];   // min product ending at i

        dp[0] = nums[0];
        minDp[0] = nums[0];

        int result = nums[0];

        for (int i = 1; i < n; i++) {

            dp[i] = Math.max(
                        nums[i],
                        Math.max(dp[i - 1] * nums[i], minDp[i - 1] * nums[i])
                    );

            minDp[i] = Math.min(
                        nums[i],
                        Math.min(dp[i - 1] * nums[i], minDp[i - 1] * nums[i])
                    );

            result = Math.max(result, dp[i]);

            System.out.println("dp[" + i + "] = " + dp[i]);
        }

        return result;
    }
}
