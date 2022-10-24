String[] array1 = {"a", "b", "c", "d", "e", "f"};
String[] array2 = {"b", "d", "f"};

List<String> list = new ArrayList<String>(Arrays.asList(array1));
list.removeAll(Arrays.asList(array2));

array1 = list.toArray(new String[list.size()]);