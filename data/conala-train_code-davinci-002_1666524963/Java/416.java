List<String> list = new ArrayList<>();
list.add("1");
list.add("2");
list.add("3");
list.add("a");
list.add("b");
list.add("c");

list.removeIf(s -> !s.matches("\\d+"));