public class Test {
 
    public static void main(String[] args) {
        String[] filenames = { "http://example.com/download.tar.gz",
                               "CharacterModel.3DS",
                               ".desktop",
                               "document",
                               "document.txt_backup",
                               "/etc/pam.d/login"
        };

        for (String filename : filenames) {
            String ext = "null";
            int idx = filename.lastIndexOf('.');
            if (idx != -1) {
                String tmp = filename.substring(idx);
                if (tmp.matches("\\.[a-zA-Z0-9]+")) {
                    ext = tmp;
                }
            }
            System.out.println(filename + " -> " + ext);
        }
    }
}