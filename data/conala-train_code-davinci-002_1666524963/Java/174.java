public static boolean containsNonAscii(String str) {
    return !str.matches("\\p{ASCII}+");
}