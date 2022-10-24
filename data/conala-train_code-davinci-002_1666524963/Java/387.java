String name = "John Doe";
Pattern pattern = Pattern.compile("^[A-Z][a-z]+\\s[A-Z][a-z]+$");
Matcher matcher = pattern.matcher(name);
if (matcher.matches()) {
    System.out.println("Name is valid");
} else {
    System.out.println("Name is invalid");
}