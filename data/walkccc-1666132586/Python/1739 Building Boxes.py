class Solution:
  def minimumBoxes(self, n: int) -> int:
    nBoxes = 0
    nextTouchings = 0   # J
    currLevelBoxes = 0  # 1 + 2 + ... + j

    # Find min j s.t. nBoxes = 1 + (1 + 2) + ... + (1 + 2 + ... + j) >= n
    while nBoxes < n:
      nextTouchings += 1
      currLevelBoxes += nextTouchings
      nBoxes += currLevelBoxes

    # If nBoxes = n, the answer is currLevelBoxes = 1 + 2 + ... + j
    if nBoxes == n:
      return currLevelBoxes

    # Otherwise we need to remove boxes in current level and rebuild it
    nBoxes -= currLevelBoxes
    currLevelBoxes -= nextTouchings
    nextTouchings = 0

    while nBoxes < n:
      nextTouchings += 1
      nBoxes += nextTouchings

    return currLevelBoxes + nextTouchings