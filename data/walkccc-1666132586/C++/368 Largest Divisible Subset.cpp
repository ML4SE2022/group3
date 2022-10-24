class Solution {
 public:
  vector<int> largestDivisibleSubset(vector<int>& nums) {
    const int n = nums.size();
    vector<int> ans;
    // sizeEndsAt[i] := largest size ends at nums[i]
    vector<int> sizeEndsAt(n, 1);
    // prevIndex[i] := the best index s.t.
    // 1. nums[i] % nums[prevIndex[i]] == 0 and
    // 2. can increase the size of the subset
    vector<int> prevIndex(n, -1);
    int maxSize = 0;  // Max size of the subset
    int index = -1;   // Track the best ending index

    sort(begin(nums), end(nums));

    // Fix max ending num in the subset first
    for (int i = 0; i < n; ++i) {
      for (int j = i - 1; j >= 0; --j)
        if (nums[i] % nums[j] == 0 && sizeEndsAt[i] < sizeEndsAt[j] + 1) {
          sizeEndsAt[i] = sizeEndsAt[j] + 1;
          prevIndex[i] = j;
        }
      // Find a new subset that has a bigger size
      if (maxSize < sizeEndsAt[i]) {
        maxSize = sizeEndsAt[i];
        index = i;  // Update the best ending index
      }
    }

    // Loop from back to front
    while (index != -1) {
      ans.push_back(nums[index]);
      index = prevIndex[index];
    }

    return ans;
  }
};