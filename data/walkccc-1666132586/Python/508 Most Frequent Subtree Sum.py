class Solution:
  def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []

    count = Counter()

    def dfs(root: Optional[TreeNode]) -> int:
      if not root:
        return 0

      summ = root.val + dfs(root.left) + dfs(root.right)
      count[summ] += 1
      return summ

    dfs(root)
    maxFreq = max(count.values())
    return [summ for summ in count if count[summ] == maxFreq]