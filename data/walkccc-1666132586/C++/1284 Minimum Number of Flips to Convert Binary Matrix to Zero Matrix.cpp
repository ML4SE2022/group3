class Solution {
 public:
  int minFlips(vector<vector<int>>& mat) {
    const int m = mat.size();
    const int n = mat[0].size();
    const int hashed = hash(mat, m, n);
    if (hashed == 0)
      return 0;

    const vector<int> dirs{0, 1, 0, -1, 0};
    queue<int> q{{hashed}};
    unordered_set<int> seen{hashed};

    for (int step = 1; !q.empty(); ++step) {
      for (int sz = q.size(); sz > 0; --sz) {
        const int curr = q.front();
        q.pop();
        for (int i = 0; i < m; ++i) {
          for (int j = 0; j < n; ++j) {
            int next = curr ^ 1 << (i * n + j);
            // Flip four neighbors
            for (int k = 0; k < 4; ++k) {
              const int x = i + dirs[k];
              const int y = j + dirs[k + 1];
              if (x < 0 || x == m || y < 0 || y == n)
                continue;
              next ^= 1 << (x * n + y);
            }
            if (next == 0)
              return step;
            if (seen.count(next))
              continue;
            q.push(next);
            seen.insert(next);
          }
        }
      }
    }

    return -1;
  }

 private:
  int hash(const vector<vector<int>>& mat, int m, int n) {
    int hashed = 0;
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (mat[i][j])
          hashed |= 1 << (i * n + j);
    return hashed;
  }
};