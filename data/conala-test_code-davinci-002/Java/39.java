public static int lastIndexOf(String str, char ch) {
    for (int i = str.length() - 1; i >= 0; i--) {
        if (str.charAt(i) == ch) {
            return i;
        }
    }
    return -1;
}