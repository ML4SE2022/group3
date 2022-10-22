class Solution {
  public int minimizeXor(int num1, int num2) {
    final int kMaxDigit = 30;
    int bits = Integer.bitCount(num2);
    // can turn off all bits in num1
    if (Integer.bitCount(num1) == bits)
      return num1;

    int ans = 0;

    // turn off MSB if we have bits quota
    for (int i = kMaxDigit - 1; i >= 0; --i)
      if ((num1 >> i & 1) == 1) {
        ans |= 1 << i;
        if (--bits == 0)
          return ans;
      }

    // turn on LSB if we still have bits
    for (int i = 0; i < kMaxDigit; ++i)
      if ((num1 >> i & 1) == 0) {
        ans |= 1 << i;
        if (--bits == 0)
          return ans;
      }

    return ans;
  }
}