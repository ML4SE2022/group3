List<Integer> indexes = IntStream.range(0, list.size())
    .filter(i -> list.get(i))
    .boxed()
    .collect(Collectors.toList());