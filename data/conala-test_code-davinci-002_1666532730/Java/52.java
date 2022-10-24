List<List<Integer>> list = new ArrayList<>();
list.add(Arrays.asList(1, 2, 3));
list.add(Arrays.asList(4, 5, 6));
list.add(Arrays.asList(7, 8, 9));

List<Integer> flatList = list.stream()
    .flatMap(Collection::stream)
    .collect(Collectors.toList());