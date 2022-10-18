class Solution {
 public:
  int bagOfTokensScore(vector<int>& tokens, int power) {
    int ans = 0;
    int score = 0;
    int i = 0;                  // Index of smallest token
    int j = tokens.size() - 1;  // Index of largest token

    sort(begin(tokens), end(tokens));

    while (i <= j && (power >= tokens[i] || score)) {
      while (i <= j && power >= tokens[i]) {
        // Play the smallest face up
        power -= tokens[i++];
        ++score;
      }
      ans = max(ans, score);
      if (i <= j && score) {
        // Play the largest face down
        power += tokens[j--];
        --score;
      }
    }

    return ans;
  }
};