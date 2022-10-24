Map<String, Map<String, String>> map = list.stream()
    .collect(Collectors.groupingBy(
        e -> e.get("id"),
        Collectors.toMap(
            e -> e.get("key"),
            e -> e.get("value")
        )
    ));