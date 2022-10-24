class Solution:
  def totalSteps(self, nums: List[int]) -> int:
    # dp[i] := # Of steps to remove nums[i]
    dp = [0] * len(nums)
    stack = []

    for i, num in enumerate(nums):
      step = 1
      while stack and nums[stack[-1]] <= num:
        step = max(step, dp[stack.pop()] + 1)
      if stack:
        dp[i] = step
      stack.append(i)

    return max(dp)