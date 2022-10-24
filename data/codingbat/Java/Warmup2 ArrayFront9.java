public boolean arrayFront9(int[] nums) {
  int end = nums.length;
  if (end > 4) end = 4;

  for (int i=0; i<end; i++) {
    if (nums[i] == 9) return true;
  }

  return false;
}