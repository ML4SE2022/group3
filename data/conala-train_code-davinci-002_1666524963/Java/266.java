String sql = "SELECT * FROM users WHERE id IN (?)";
PreparedStatement stmt = conn.prepareStatement(sql);
stmt.setArray(1, conn.createArrayOf("integer", new Integer[]{1, 2, 3}));
ResultSet rs = stmt.executeQuery();