List<List<String>> list = new ArrayList<>();
list.add(Arrays.asList("a", "b", "c"));
list.add(Arrays.asList("d", "e", "f"));
list.add(Arrays.asList("g", "h", "i"));

list.stream()
    .map(l -> l.stream()
        .map(s -> s.replace("a", "A"))
        .collect(Collectors.toList()))
    .collect(Collectors.toList());