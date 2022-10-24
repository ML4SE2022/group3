String arabicText = "العربية";
String englishText = "English";
String mixedText = "العربية English";

String arabicTextRegex = "[\u0600-\u06FF]+";
String englishTextRegex = "[a-zA-Z]+";

System.out.println(arabicText.matches(arabicTextRegex)); // true
System.out.println(englishText.matches(arabicTextRegex)); // false
System.out.println(mixedText.matches(arabicTextRegex)); // false

System.out.println(arabicText.matches(englishTextRegex)); // false
System.out.println(englishText.matches(englishTextRegex)); // true
System.out.println(mixedText.matches(englishTextRegex)); // false