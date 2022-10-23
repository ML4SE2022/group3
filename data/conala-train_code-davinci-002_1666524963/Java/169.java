List<String> list = new ArrayList<>();
list.add("a");
list.add("b");
list.add("c");

List<List<String>> listOfLists = new ArrayList<>();
listOfLists.add(list);
listOfLists.add(list);
listOfLists.add(list);

List<String> mergedList = listOfLists.stream()
        .flatMap(Collection::stream)
        .collect(Collectors.toList());