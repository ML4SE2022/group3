class Solution:
  def isConvex(self, points: List[List[int]]) -> bool:
    # Pq x qr
    def getCross(p: List[int], q: List[int], r: List[int]):
      return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    sign = 0
    for i in range(len(points)):
      cross = getCross(points[i - 2], points[i - 1], points[i])
      if cross == 0:  # P, q, r are collinear
        continue
      if sign == 0:  # Find first cross that's not 0
        sign = cross
      elif cross * sign < 0:
        return False

    return True