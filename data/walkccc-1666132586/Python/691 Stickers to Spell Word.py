class Solution:
  def minStickers(self, stickers: List[str], target: str) -> int:
    n = len(target)
    maxMask = 1 << n
    # dp[i] := min # Of stickers to spell out i,
    # Where i is the bit representation of target
    dp = [math.inf] * maxMask
    dp[0] = 0

    for mask in range(maxMask):
      if dp[mask] == math.inf:
        continue
      # Try to expand from `mask` by using each sticker
      for sticker in stickers:
        superMask = mask
        for c in sticker:
          for i, t in enumerate(target):
            # Try to apply it on a missing char
            if c == t and not (superMask >> i & 1):
              superMask |= 1 << i
              break
        dp[superMask] = min(dp[superMask], dp[mask] + 1)

    return -1 if dp[-1] == math.inf else dp[-1]