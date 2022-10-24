class Solution {
 public:
  string capitalizeTitle(string title) {
    transform(begin(title), end(title), begin(title), ::tolower);

    int i = 0;  // Point to the start of a word
    int j = 0;  // Point to the end of a word

    while (j < title.length()) {
      while (j < title.length() && title[j] != ' ')
        ++j;
      if (j - i > 2)
        title[i] = toupper(title[i]);
      i = j + 1;
      ++j;  // Skip the space
    }

    return title;
  }
};