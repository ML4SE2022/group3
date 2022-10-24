File dir = new File("/home/user/Documents");
File[] files = dir.listFiles(new FilenameFilter() {
    @Override
    public boolean accept(File dir, String name) {
        return name.endsWith(".txt");
    }
});