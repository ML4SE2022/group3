public static int getMaxStringLength(List<List<String>> list) {
    int maxLength = 0;
    for (List<String> subList : list) {
        for (String s : subList) {
            if (s.length() > maxLength) {
                maxLength = s.length();
            }
        }
    }
    return maxLength;
}