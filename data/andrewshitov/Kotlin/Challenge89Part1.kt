fun gcd(a: Int, b: Int): Int {
    var x = a
    var y = b

    while (y != 0) {
        val t = y
        y = x % y
        x = t
    }

    return x
}

fun main(args: Array) {
    var n: Int
    if (args.size == 1)
        n = args[0].toInt()
    else
        n = 3

    var s = 0
    for (x in 1..n) {
        for (y in x + 1 .. n) {
            s += gcd(x, y)
        }
    }

    println(s)
}