import math.BigInt

object Main {
    def main(args: Array[String]): Unit = {
        var n: Int = if (args.size == 1) args(0).toInt else 3

        var s: BigInt = 0
        for (x <- 1 to n) {
            for (y <- x + 1 to n) {
                s = s + BigInt(x).gcd(y)
            }
        }

        println(s)
    }
}