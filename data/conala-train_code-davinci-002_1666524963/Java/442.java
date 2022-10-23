List<List<String>> listOfLists = new ArrayList<>();
List<String> list1 = new ArrayList<>();
list1.add("a");
list1.add("b");
list1.add("c");
List<String> list2 = new ArrayList<>();
list2.add("a");
list2.add("b");
list2.add("c");
listOfLists.add(list1);
listOfLists.add(list2);

List<String> result = listOfLists.stream()
    .flatMap(Collection::stream)
    .distinct()
    .collect(Collectors.toList());