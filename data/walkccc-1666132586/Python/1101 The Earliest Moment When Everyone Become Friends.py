class UnionFind:
  def __init__(self, n: int):
    self.count = n
    self.id = list(range(n))
    self.rank = [0] * n

  def union(self, u: int, v: int) -> None:
    i = self._find(u)
    j = self._find(v)
    if i == j:
      return
    if self.rank[i] > self.rank[j]:
      i, j = j, i
    elif self.rank[i] == self.rank[j]:
      self.rank[j] += 1
    self.id[i] = j
    self.count -= 1

  def getCount(self) -> int:
    return self.count

  def _find(self, u: int) -> int:
    if self.id[u] != u:
      self.id[u] = self._find(self.id[u])
    return self.id[u]


class Solution:
  def earliestAcq(self, logs: List[List[int]], n: int) -> int:
    uf = UnionFind(n)

    # Sort `logs` by timestamp.
    for timestamp, x, y in logs:
      uf.union(x, y)
      if uf.getCount() == 1:
        return timestamp

    return -1