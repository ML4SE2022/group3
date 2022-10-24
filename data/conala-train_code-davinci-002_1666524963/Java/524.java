public static void main(String[] args) throws Exception {
    Class.forName("org.sqlite.JDBC");
    Connection conn = DriverManager.getConnection("jdbc:sqlite:test.db");
    Statement stat = conn.createStatement();
    ResultSet rs = stat.executeQuery("select * from tbl1;");
    ResultSetMetaData rsmd = rs.getMetaData();
    int columnCount = rsmd.getColumnCount();
    for (int i = 1; i <= columnCount; i++ ) {
      String name = rsmd.getColumnName(i);
      System.out.println(name);
    }
}