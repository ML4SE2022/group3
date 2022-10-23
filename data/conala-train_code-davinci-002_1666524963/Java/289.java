File dir = new File("/path/to/dir");
File[] files = dir.listFiles();
for (File file : files) {
    if (file.isFile()) {
        System.out.println(file.getName());
    }
}