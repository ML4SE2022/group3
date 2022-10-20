List<String> list = new ArrayList<>();
list.add("1");
list.add("2");
list.add("3");

List<Integer> intList = list.stream().map(Integer::parseInt).collect(Collectors.toList());