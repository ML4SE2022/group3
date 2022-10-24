List<String> list = Arrays.asList("a", "b", "c", "d", "a", "b", "c", "d");

int count = 0;
for (String element : list) {
    if (element.equals("a")) {
        count++;
    }
}

System.out.println(count);