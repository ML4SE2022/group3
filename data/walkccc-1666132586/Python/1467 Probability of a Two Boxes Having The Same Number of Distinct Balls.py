from enum import Enum


class BoxCase(Enum):
  EqualDistantBalls = 0
  EqualBalls = 1


class Solution:
  def getProbability(self, balls: List[int]) -> float:
    n = sum(balls) // 2
    fact = [1, 1, 2, 6, 24, 120, 720]

    def cases(i: int, ballsCountA: int, ballsCountB: int,
              colorsCountA: int, colorsCountB, boxCase: BoxCase) -> float:
      if ballsCountA > n or ballsCountB > n:
        return 0
      if i == len(balls):
        return 1 if boxCase == BoxCase.EqualBalls else colorsCountA == colorsCountB

      ans = 0.0

      # Balls taken from A for `balls[i]`
      for ballsTakenA in range(balls[i] + 1):
        ballsTakenB = balls[i] - ballsTakenA
        newcolorsCountA = colorsCountA + (ballsTakenA > 0)
        newcolorsCountB = colorsCountB + (ballsTakenB > 0)
        ans += cases(i + 1, ballsCountA + ballsTakenA, ballsCountB + ballsTakenB,
                     newcolorsCountA, newcolorsCountB, boxCase) / \
            (fact[ballsTakenA] * fact[ballsTakenB])

      return ans

    return cases(0, 0, 0, 0, 0, BoxCase.EqualDistantBalls) / \
        cases(0, 0, 0, 0, 0, BoxCase.EqualBalls)