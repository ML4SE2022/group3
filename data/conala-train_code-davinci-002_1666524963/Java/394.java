List<Integer> list = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
List<Integer> greaterThanFive = list.stream().filter(i -> i > 5).collect(Collectors.toList());