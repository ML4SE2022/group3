public static boolean containsList(List<Object> list) {
    for (Object o : list) {
        if (o instanceof List) {
            return true;
        }
    }
    return false;
}