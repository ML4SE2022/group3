public static int countEnd(String str, char c) {
    int count = 0;
    for (int i = str.length() - 1; i >= 0; i--) {
        if (str.charAt(i) == c) {
            count++;
        } else {
            break;
        }
    }
    return count;
}