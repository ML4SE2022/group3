String dateString = "2018-01-01T00:00:00.000Z";
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");
LocalDateTime dateTime = LocalDateTime.parse(dateString, formatter);