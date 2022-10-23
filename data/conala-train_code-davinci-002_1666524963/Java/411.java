List<String> keys = new ArrayList<>();
for (Map.Entry<String, Map<String, String>> entry : dict.entrySet()) {
    keys.addAll(entry.getValue().keySet());
}