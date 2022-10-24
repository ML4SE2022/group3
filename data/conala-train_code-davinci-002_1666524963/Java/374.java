public static <T> T nthToLast(LinkedList<T> list, int n) {
    if (list.isEmpty()) {
        return null;
    }
    LinkedList<T> reversed = new LinkedList<T>();
    while (!list.isEmpty()) {
        reversed.addFirst(list.removeFirst());
    }
    T result = null;
    for (int i = 0; i < n; i++) {
        result = reversed.removeFirst();
    }
    while (!reversed.isEmpty()) {
        list.addFirst(reversed.removeFirst());
    }
    return result;
}