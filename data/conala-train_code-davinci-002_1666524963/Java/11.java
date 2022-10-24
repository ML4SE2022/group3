public class AlphanumericSort {
    public static void main(String[] args) {
        List<String> list = Arrays.asList("a1", "a10", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9");
        Collections.sort(list, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return extractInt(o1) - extractInt(o2);
            }

            int extractInt(String s) {
                String num = s.replaceAll("\\D", "");
                // return 0 if no digits found
                return num.isEmpty() ? 0 : Integer.parseInt(num);
            }
        });
        System.out.println(list);
    }
}