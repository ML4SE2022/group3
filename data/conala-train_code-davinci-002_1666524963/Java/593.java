Map<String, String> map = new HashMap<>();
map.put("foo", "bar");
map.put("foobar", "baz");

map.entrySet().stream()
    .filter(e -> e.getKey().contains("foo"))
    .forEach(e -> System.out.println(e.getKey() + ": " + e.getValue()));