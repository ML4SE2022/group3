List<String> list = Arrays.asList("1", "2", "3");
List<Integer> intList = list.stream().map(Integer::parseInt).collect(Collectors.toList());