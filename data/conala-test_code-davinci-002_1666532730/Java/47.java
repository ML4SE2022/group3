public static int longestWord(String[] words) {
    int maxLength = 0;
    for (String word : words) {
        maxLength = Math.max(maxLength, word.length());
    }
    return maxLength;
}