public static void main(String[] args) {
    Cluster cluster = Cluster.builder().addContactPoint("127.0.0.1").build();
    Session session = cluster.connect("mykeyspace");
    ResultSet results = session.execute("SELECT * FROM mytable");
    for (Row row : results) {
        System.out.format("%s %d\n", row.getString("mycolumn"), row.getInt("mycolumn2"));
    }
}