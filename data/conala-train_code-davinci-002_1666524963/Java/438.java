List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
boolean allEven = numbers.stream().allMatch(n -> n % 2 == 0);