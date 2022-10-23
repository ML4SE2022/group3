Map<String, Double> map = new HashMap<>();
map.put("a", 1.0);
map.put("b", 2.0);
map.put("c", 3.0);

double sum = 0.0;
for (Double value : map.values()) {
    sum += value;
}
double average = sum / map.size();