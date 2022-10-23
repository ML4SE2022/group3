String fileName = "file.txt";
String line = null;
StringBuilder sb = new StringBuilder();

try {
    FileReader fileReader = new FileReader(fileName);
    BufferedReader bufferedReader = new BufferedReader(fileReader);

    while((line = bufferedReader.readLine()) != null) {
        sb.append(line.replaceAll("\\^M", ""));
    }

    bufferedReader.close();
}
catch(FileNotFoundException ex) {
    System.out.println("Unable to open file '" + fileName + "'");
}
catch(IOException ex) {
    System.out.println("Error reading file '" + fileName + "'");
}