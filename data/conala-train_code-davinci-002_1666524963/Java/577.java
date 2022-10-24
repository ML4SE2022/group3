List<String> stringList = Arrays.asList("1", "2", "3");
List<Integer> integerList = new ArrayList<>();
for (String s : stringList) {
    integerList.add(Integer.parseInt(s));
}