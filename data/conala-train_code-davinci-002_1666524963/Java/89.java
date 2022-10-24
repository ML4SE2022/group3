File file = new File("/path/to/file");
File dir = new File("/path/to/dir");

file.getCanonicalPath().startsWith(dir.getCanonicalPath());