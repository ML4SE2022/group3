List<List<Integer>> list = new ArrayList<>();
list.add(Arrays.asList(1, 2, 3));
list.add(Arrays.asList(4, 5, 6));
list.add(Arrays.asList(7, 8, 9));

List<List<Integer>> zipped = IntStream.range(0, list.get(0).size())
        .mapToObj(i -> list.stream().map(l -> l.get(i)).collect(Collectors.toList()))
        .collect(Collectors.toList());