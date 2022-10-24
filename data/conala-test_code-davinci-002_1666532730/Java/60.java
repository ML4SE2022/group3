int index = IntStream.range(0, list.size())
                     .filter(i -> list.get(i))
                     .findFirst()
                     .orElse(-1);