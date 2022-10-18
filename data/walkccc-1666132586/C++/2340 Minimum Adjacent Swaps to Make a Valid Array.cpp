class Solution {
 public:
  int minimumSwaps(vector<int>& nums) {
    const int minIndex = getLeftmostMinIndex(nums);
    const int maxIndex = getRightmostMaxIndex(nums);
    const int swaps = minIndex + (nums.size() - 1 - maxIndex);
    return minIndex <= maxIndex ? swaps : swaps - 1;
  }

 private:
  int getLeftmostMinIndex(const vector<int>& nums) {
    int min = nums.front();
    int minIndex = 0;
    for (int i = 1; i < nums.size(); ++i)
      if (nums[i] < min) {
        min = nums[i];
        minIndex = i;
      }
    return minIndex;
  }

  int getRightmostMaxIndex(const vector<int>& nums) {
    int max = nums.back();
    int maxIndex = nums.size() - 1;
    for (int i = nums.size() - 2; i >= 0; --i)
      if (nums[i] > max) {
        max = nums[i];
        maxIndex = i;
      }
    return maxIndex;
  }
};