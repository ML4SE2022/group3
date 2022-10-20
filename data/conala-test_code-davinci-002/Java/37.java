File dir = new File("/path/to/dir");
File[] files = dir.listFiles();
Random rand = new Random();
File file = files[rand.nextInt(files.length)];