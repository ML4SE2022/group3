class Solution:
  def replaceElements(self, arr: List[int]) -> List[int]:
    maxOfRight = -1
    for i in reversed(range(len(arr))):
      arr[i], maxOfRight = maxOfRight, max(maxOfRight, arr[i])
    return arr