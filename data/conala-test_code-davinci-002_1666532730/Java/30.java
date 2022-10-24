public static boolean all(String s, Predicate<Character> p) {
    for (int i = 0; i < s.length(); i++) {
        if (!p.test(s.charAt(i))) {
            return false;
        }
    }
    return true;
}