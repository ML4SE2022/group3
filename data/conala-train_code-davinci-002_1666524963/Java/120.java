Map<String, Integer> map = new HashMap<>();
map.put("a", 1);
map.put("b", 2);
map.put("c", 3);

int sum = 0;
for (Integer value : map.values()) {
    sum += value;
}
System.out.println(sum);