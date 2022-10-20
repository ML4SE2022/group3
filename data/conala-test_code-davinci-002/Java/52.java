List<String> list = new ArrayList<>();
list.add("a");
list.add("b");
list.add("c");
list.removeIf(s -> s.equals("b"));