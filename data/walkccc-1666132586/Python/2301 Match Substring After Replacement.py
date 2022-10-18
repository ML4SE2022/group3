class Solution:
  def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
    isMapped = [[False] * 128 for _ in range(128)]

    for old, new in mappings:
      isMapped[ord(old)][ord(new)] = True

    for i in range(len(s)):
      if self._canTransform(s, i, sub, isMapped):
        return True

    return False

  def _canTransform(self, s: str, start: int, sub: str, isMapped: List[List[bool]]) -> bool:
    if start + len(sub) > len(s):
      return False

    for i in range(len(sub)):
      a = sub[i]        # sub's char
      b = s[start + i]  # s' char
      if a != b and not isMapped[ord(a)][ord(b)]:
        return False

    return True