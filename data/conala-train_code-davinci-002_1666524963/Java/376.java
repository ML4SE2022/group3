List<String> list1 = Arrays.asList("a", "b", "c");
List<String> list2 = Arrays.asList("1", "2", "3");
List<String> list3 = Arrays.asList("x", "y", "z");

List<List<String>> lists = Arrays.asList(list1, list2, list3);

List<String> result = new ArrayList<>();
for (int i = 0; i < list1.size(); i++) {
    for (List<String> list : lists) {
        result.add(list.get(i));
    }
}

System.out.println(result);