class Solution {
 public:
  int componentValue(vector<int>& nums, vector<vector<int>>& edges) {
    const int n = nums.size();
    const int sum = accumulate(begin(nums), end(nums), 0);
    vector<vector<int>> graph(n);

    for (const vector<int>& e : edges) {
      const int u = e[0];
      const int v = e[1];
      graph[u].push_back(v);
      graph[v].push_back(u);
    }

    for (int i = n; i > 1; --i)
      // split the tree into i parts, i.e., delete (i - 1) edges
      if (sum % i == 0 && dfs(nums, graph, 0, sum / i, vector<bool>(n)) == 0)
        return i - 1;

    return 0;
  }

 private:
  constexpr static int kMax = 1'000'000'000;

  // Returns the sum of the subtree rooted at u minus the sum of the deleted
  // subtrees.
  int dfs(const vector<int>& nums, const vector<vector<int>>& graph, int u,
          int target, vector<bool>&& seen) {
    int sum = nums[u];
    seen[u] = true;

    for (const int v : graph[u]) {
      if (seen[v])
        continue;
      sum += dfs(nums, graph, v, target, move(seen));
      if (sum > target)
        return kMax;
    }

    // Delete the tree that has sum == target
    if (sum == target)
      return 0;
    return sum;
  }
};