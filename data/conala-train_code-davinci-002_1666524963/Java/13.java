public static void reverse(List<Integer> list, int start, int end) {
    if (start < 0 || end >= list.size() || start >= end) {
        return;
    }
    while (start < end) {
        int temp = list.get(start);
        list.set(start, list.get(end));
        list.set(end, temp);
        start++;
        end--;
    }
}