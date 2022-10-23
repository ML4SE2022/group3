List<String> list1 = Arrays.asList("a", "b", "c");
List<String> list2 = Arrays.asList("1", "2", "3");
List<Tuple2<String, String>> list = list1.stream()
    .flatMap(s1 -> list2.stream().map(s2 -> new Tuple2<>(s1, s2)))
    .collect(Collectors.toList());