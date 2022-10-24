public static <T> List<List<T>> splitList(List<T> list, int chunkSize) {
    List<List<T>> chunks = new ArrayList<>();
    for (int i = 0; i < list.size(); i += chunkSize) {
        chunks.add(list.subList(i, Math.min(i + chunkSize, list.size())));
    }
    return chunks;
}