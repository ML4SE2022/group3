public static int nthOccurrence(String str, char c, int n) {
    int pos = str.indexOf(c, 0);
    while (n-- > 0 && pos != -1)
        pos = str.indexOf(c, pos+1);
    return pos;
}