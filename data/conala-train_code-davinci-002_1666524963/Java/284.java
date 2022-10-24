List<String> first = Arrays.asList("a", "b", "c");
List<String> second = Arrays.asList("x", "y", "z");

List<String> result = new ArrayList<>();
result.add(first.get(0));
result.add(second.get(second.size() - 1));