int maxIndex = 0;
for (int i = 0; i < list.size(); i++) {
    if (list.get(i).getValue() > list.get(maxIndex).getValue()) {
        maxIndex = i;
    }
}