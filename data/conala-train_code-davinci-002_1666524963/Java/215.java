public static List<String> splitString(String str, int chunkSize) {
    List<String> chunks = new ArrayList<>();
    for (int i = 0; i < str.length(); i += chunkSize) {
        chunks.add(str.substring(i, Math.min(str.length(), i + chunkSize)));
    }
    return chunks;
}