class Solution {
 public:
  vector<long long> minimumCosts(vector<int>& regular, vector<int>& express,
                                 int expressCost) {
    const int n = regular.size();
    vector<long long> ans(n);
    // Min cost to reach current stop in regular route
    long long dpReg = 0;
    // Min cost to reach current stop in express route
    long long dpExp = expressCost;

    for (int i = 0; i < n; ++i) {
      const long long prevReg = dpReg;
      const long long prevExp = dpExp;
      dpReg = min(prevReg + regular[i], prevExp + 0 + regular[i]);
      dpExp = min(prevReg + expressCost + express[i], prevExp + express[i]);
      ans[i] = min(dpReg, dpExp);
    }

    return ans;
  }
};