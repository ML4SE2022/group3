public static void reverse(List<Integer> list) {
    for (int i = 0; i < list.size() / 2; i++) {
        int temp = list.get(i);
        list.set(i, list.get(list.size() - i - 1));
        list.set(list.size() - i - 1, temp);
    }
}