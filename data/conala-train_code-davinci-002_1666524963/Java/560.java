import com.google.appengine.tools.cloudstorage.GcsFileOptions;
import com.google.appengine.tools.cloudstorage.GcsFilename;
import com.google.appengine.tools.cloudstorage.GcsOutputChannel;
import com.google.appengine.tools.cloudstorage.GcsService;
import com.google.appengine.tools.cloudstorage.GcsServiceFactory;
import com.google.appengine.tools.cloudstorage.RetryParams;

import java.io.IOException;
import java.nio.channels.Channels;

public class GcsExample {

  private static final String BUCKETNAME = "my-bucket";

  private final GcsService gcsService = GcsServiceFactory.createGcsService(RetryParams.getDefaultInstance());

  public void writeFile(String filename, byte[] content) throws IOException {
    GcsFileOptions instance = GcsFileOptions.getDefaultInstance();
    GcsFilename gcsFilename = new GcsFilename(BUCKETNAME, filename);
    GcsOutputChannel outputChannel;
    outputChannel = gcsService.createOrReplace(gcsFilename, instance);
    outputChannel.write(ByteBuffer.wrap(content));
    outputChannel.close();
  }
}