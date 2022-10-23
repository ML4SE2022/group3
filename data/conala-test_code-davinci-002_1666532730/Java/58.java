MongoCursor<Document> cursor = collection.find().iterator();
while (cursor.hasNext()) {
    Document doc = cursor.next();
    for (Map.Entry<String, Object> entry : doc.entrySet()) {
        System.out.println(entry.getKey() + ": " + entry.getValue());
    }
}