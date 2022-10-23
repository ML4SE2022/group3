Collections.sort(list, new Comparator<Person>() {
    @Override
    public int compare(Person p1, Person p2) {
        int cmp = p1.getLastName().compareTo(p2.getLastName());
        if (cmp != 0) {
            return cmp;
        }
        return p1.getFirstName().compareTo(p2.getFirstName());
    }
});