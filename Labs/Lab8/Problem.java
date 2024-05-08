package Labs.Lab8;

public class Problem {
    public int coinChange(int[] coins, int amount) {
        
        int max = amount + 1;
        
        int[] dp = new int[amount + 1];
        
        for (int i = 0; i <= amount; i++) {
            dp[i] = max;
        }
        
        dp[0] = 0;

        
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }
    
}
