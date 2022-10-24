Collections.sort(files, new Comparator<File>() {
    public int compare(File f1, File f2) {
        return Long.valueOf(f1.lastModified()).compareTo(f2.lastModified());
    }
});