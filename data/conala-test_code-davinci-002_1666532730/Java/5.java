public static void createDirIfNotExists(String dir) {
    File theDir = new File(dir);
    if (!theDir.exists()) {
        System.out.println("creating directory: " + dir);
        boolean result = false;
        try {
            theDir.mkdir();
            result = true;
        } catch (SecurityException se) {
            //handle it
        }
        if (result) {
            System.out.println("DIR created");
        }
    }
}