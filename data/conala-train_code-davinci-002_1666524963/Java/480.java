List<Integer> list1 = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> list2 = Arrays.asList(3, 4, 5, 6, 7);

list1.stream()
    .filter(i -> !list2.contains(i))
    .collect(Collectors.toList());