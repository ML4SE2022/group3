class Solution:
  def numTilePossibilities(self, tiles: str) -> int:
    count = Counter(tiles)

    def dfs(count: Dict[int, int]) -> int:
      possibleSequences = 0

      for k, v in count.items():
        if v == 0:
          continue
        # Put c in the current position. We only care about the # of possible
        # sequences of letters but don't care about the actual combination.
        count[k] -= 1
        possibleSequences += 1 + dfs(count)
        count[k] += 1

      return possibleSequences

    return dfs(count)