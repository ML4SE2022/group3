// Create a query
Query query = new Query("Person");

// Add a condition
query.addFilter("address", Query.FilterOperator.EQUAL, KeyFactory.createKey("Address", "123"));

// Execute the query
DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();
PreparedQuery pq = datastore.prepare(query);

// Iterate over the results
for (Entity result : pq.asIterable()) {
  String firstName = (String) result.getProperty("firstName");
  String lastName = (String) result.getProperty("lastName");
  System.out.println(firstName + " " + lastName + " lives at " + result.getProperty("address"));
}