class Solution:
  def climbStairs(self, n: int) -> int:
    # dp[i] := # Of distinct ways to climb to i-th stair
    dp = [1, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
      dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]