public static int convertToBase10(String s) {
    int result = 0;
    for (int i = 0; i < s.length(); i++) {
        result = result * 2 + (s.charAt(i) - '0');
    }
    return result;
}