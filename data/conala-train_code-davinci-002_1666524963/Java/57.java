List<Integer> hexBytes = Arrays.asList("0x01", "0x02", "0x03");
List<Integer> hexInts = hexBytes.stream().map(Integer::decode).collect(Collectors.toList());