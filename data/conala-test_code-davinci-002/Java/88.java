public static <T> List<List<T>> unzip(List<List<T>> list) {
    List<List<T>> result = new ArrayList<>();
    for (int i = 0; i < list.get(0).size(); i++) {
        List<T> subList = new ArrayList<>();
        for (List<T> sub : list) {
            subList.add(sub.get(i));
        }
        result.add(subList);
    }
    return result;
}