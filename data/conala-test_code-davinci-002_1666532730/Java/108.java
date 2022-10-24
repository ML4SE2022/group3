List<List<Integer>> listOfLists = new ArrayList<>();
listOfLists.add(Arrays.asList(1, 2, 3));
listOfLists.add(Arrays.asList(4, 5, 6));
listOfLists.add(Arrays.asList(7, 8, 9));

List<Integer> mergedList = listOfLists.stream()
    .flatMap(Collection::stream)
    .collect(Collectors.toList());