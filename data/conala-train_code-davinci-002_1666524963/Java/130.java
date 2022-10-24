public static boolean isInDictionary(String word, Map<String, List<String>> dictionary) {
    for (String key : dictionary.keySet()) {
        if (dictionary.get(key).contains(word)) {
            return true;
        }
    }
    return false;
}