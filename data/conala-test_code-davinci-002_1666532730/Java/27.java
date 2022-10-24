String fileName = "file.txt";
String line = null;

try {
    FileReader fileReader = new FileReader(fileName);
    BufferedReader bufferedReader = new BufferedReader(fileReader);

    while((line = bufferedReader.readLine()) != null) {
        System.out.println(line);
    }

    bufferedReader.close();
}
catch(FileNotFoundException ex) {
    System.out.println("Unable to open file '" + fileName + "'");
}
catch(IOException ex) {
    System.out.println("Error reading file '" + fileName + "'");
}