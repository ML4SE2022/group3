class Solution:
  def numDupDigitsAtMostN(self, n: int) -> int:
    return n - self._countSpecialNumbers(n)

  def _countSpecialNumbers(self, n: int) -> int:
    s = str(n)
    digitSize = int(log10(n)) + 1

    # Dp(i, j, k) := # Of special integers that beto the interval
    # [0, 10^i] with `usedMask` j, where k is 0/1 tight constraint
    @functools.lru_cache(None)
    def dp(digitSize: int, usedMask: int, isTight: bool) -> int:
      if digitSize == 0:
        return 1

      ans = 0
      maxDigit = ord(s[len(s) - digitSize]) - ord('0') if isTight else 9

      for digit in range(maxDigit + 1):
        # `digit` is used
        if usedMask >> digit & 1:
          continue
        # Use `digit` now
        nextIsTight = isTight and (digit == maxDigit)
        if usedMask == 0 and digit == 0:  # don't count leading 0s as used
          ans += dp(digitSize - 1, usedMask, nextIsTight)
        else:
          ans += dp(digitSize - 1, usedMask | 1 << digit, nextIsTight)

      return ans

    return dp(digitSize, 0, True) - 1  # - 0