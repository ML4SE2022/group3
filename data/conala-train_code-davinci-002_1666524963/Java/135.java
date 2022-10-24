List<String> list = new ArrayList<String>();
list.add("a");
list.add("b");
list.add("c");
list.add("d");
list.add("e");
list.add("f");
list.add("g");
list.add("h");
list.add("i");
list.add("j");
list.add("k");
list.add("l");
list.add("m");
list.add("n");
list.add("o");
list.add("p");
list.add("q");
list.add("r");
list.add("s");
list.add("t");
list.add("u");
list.add("v");
list.add("w");
list.add("x");
list.add("y");
list.add("z");

Collections.sort(list, new Comparator<String>() {
    @Override
    public int compare(String o1, String o2) {
        if (o1.matches("[a-m].*") && o2.matches("[n-z].*")) {
            return -1;
        } else if (o1.matches("[n-z].*") && o2.matches("[a-m].*")) {
            return 1;
        } else {
            return o1.compareTo(o2);
        }
    }
});

System.out.println(list);