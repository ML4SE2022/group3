public static float hexToFloat(String hex) {
    return Float.intBitsToFloat(Integer.parseInt(hex, 16));
}