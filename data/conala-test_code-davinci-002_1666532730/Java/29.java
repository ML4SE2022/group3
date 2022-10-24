List<String> list = new ArrayList<>();
list.add("2019-01-01");
list.add("2019-01-02");
list.add("2019-01-03");
list.add("2019-01-04");
list.add("2019-01-05");
list.add("2019-01-06");
list.add("2019-01-07");
list.add("2019-01-08");
list.add("2019-01-09");
list.add("2019-01-10");
list.add("2019-01-11");
list.add("2019-01-12");
list.add("2019-01-13");
list.add("2019-01-14");
list.add("2019-01-15");
list.add("2019-01-16");
list.add("2019-01-17");
list.add("2019-01-18");
list.add("2019-01-19");
list.add("2019-01-20");
list.add("2019-01-21");
list.add("2019-01-22");
list.add("2019-01-23");
list.add("2019-01-24");
list.add("2019-01-25");
list.add("2019-01-26");
list.add("2019-01-27");
list.add("2019-01-28");
list.add("2019-01-29");
list.add("2019-01-30");
list.add("2019-01-31");

Collections.sort(list, new Comparator<String>() {
    @Override
    public int compare(String o1, String o2) {
        try {
            return new SimpleDateFormat("yyyy-MM-dd").parse(o1).compareTo(new SimpleDateFormat("yyyy-MM-dd").parse(o2));
        } catch (ParseException e) {
            e.printStackTrace();
        }
        return 0;
    }
});

for (String s : list) {
    System.out.println(s);
}