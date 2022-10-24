public static String removeFinalCharacters(String str, int n) {
    if (str.length() <= n) {
        return "";
    }
    return removeFinalCharacters(str.substring(0, str.length() - 1), n);
}