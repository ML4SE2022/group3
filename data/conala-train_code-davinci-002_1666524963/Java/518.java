File[] files = new File("/path/to/directory").listFiles(new FilenameFilter() {
    @Override
    public boolean accept(File dir, String name) {
        return name.endsWith(".txt");
    }
});