List<String> list = Arrays.asList("a", "b", "c");
List<String> newList = list.stream().map(s -> "x" + s).collect(Collectors.toList());