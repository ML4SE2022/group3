FileWriter fw = new FileWriter("output.txt", true);
BufferedWriter bw = new BufferedWriter(fw);
bw.write("Hello World");
bw.newLine();
bw.close();