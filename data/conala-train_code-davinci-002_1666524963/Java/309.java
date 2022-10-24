List<String> list1 = Arrays.asList("a", "b", "c");
List<String> list2 = Arrays.asList("b", "c", "d");

boolean anyMatch = list1.stream().anyMatch(list2::contains);