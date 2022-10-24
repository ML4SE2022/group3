List<String> list1 = Arrays.asList("A", "B", "C");
List<String> list2 = Arrays.asList("D", "E", "F");
List<String> list3 = Arrays.asList("G", "H", "I");

List<String> result = Stream.of(list1, list2, list3)
    .flatMap(Collection::stream)
    .collect(Collectors.toList());