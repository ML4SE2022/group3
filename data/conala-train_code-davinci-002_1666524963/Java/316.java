public class SortList {
    public static void main(String[] args) {
        List<String> list = Arrays.asList("a", "b", "c", "d", "e");
        List<Integer> order = Arrays.asList(3, 1, 4, 2, 0);
        List<String> sorted = new ArrayList<>(list.size());
        for (int i = 0; i < list.size(); i++) {
            sorted.add(null);
        }
        for (int i = 0; i < list.size(); i++) {
            sorted.set(order.get(i), list.get(i));
        }
        System.out.println(sorted);
    }
}