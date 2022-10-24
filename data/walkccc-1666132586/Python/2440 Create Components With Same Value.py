class Solution:
  def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
    kMax = 1_000_000_000
    n = len(nums)
    summ = sum(nums)
    graph = [[] for _ in range(n)]

    for u, v in edges:
      graph[u].append(v)
      graph[v].append(u)

    # Returns the sum of the subtree rooted at u minus the sum of the deleted subtrees.
    def dfs(u: int, target: int, seen: Set[bool]) -> int:
      summ = nums[u]
      seen.add(u)

      for v in graph[u]:
        if v in seen:
          continue
        summ += dfs(v, target, seen)
        if summ > target:
          return kMax

      # Delete the tree that has sum == target
      if summ == target:
        return 0
      return summ

    for i in range(n, 1, -1):
      # split the tree into i parts, i.e., delete (i - 1) edges
      if summ % i == 0 and dfs(0, summ // i, set()) == 0:
        return i - 1

    return 0