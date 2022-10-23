public static int sum(List<Object> list) {
    int sum = 0;
    for (Object obj : list) {
        if (obj instanceof Integer) {
            sum += (Integer) obj;
        } else if (obj instanceof List) {
            sum += sum((List<Object>) obj);
        }
    }
    return sum;
}