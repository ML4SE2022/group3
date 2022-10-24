public static float stringToFloat(String s) {
    return Float.intBitsToFloat(s.hashCode());
}