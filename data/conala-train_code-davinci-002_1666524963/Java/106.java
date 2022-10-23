public static int countWord(String word, String sentence) {
    int count = 0;
    for (String s : sentence.split(" ")) {
        if (s.equals(word)) {
            count++;
        }
    }
    return count;
}