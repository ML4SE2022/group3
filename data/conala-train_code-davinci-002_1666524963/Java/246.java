URL url = new URL("http://www.example.com/example.txt");
ReadableByteChannel rbc = Channels.newChannel(url.openStream());
FileOutputStream fos = new FileOutputStream("example.txt");
fos.getChannel().transferFrom(rbc, 0, Long.MAX_VALUE);