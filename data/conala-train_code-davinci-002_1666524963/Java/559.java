String[] array = {"a", "b", "c", "d", "e"};
String[] result = Arrays.stream(array)
                        .map(s -> s.substring(0, 1))
                        .toArray(String[]::new);