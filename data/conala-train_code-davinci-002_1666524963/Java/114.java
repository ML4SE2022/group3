String rreplace(String s, String toReplace, String replacement) {
    int pos = s.lastIndexOf(toReplace);
    if (pos > -1) {
        return s.substring(0, pos)
             + replacement
             + s.substring(pos + toReplace.length(), s.length());
    } else {
        return s;
    }
}