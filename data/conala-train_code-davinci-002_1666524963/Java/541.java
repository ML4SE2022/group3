byte[] key = "key".getBytes();
byte[] value = "value".getBytes();

// put
client.put(key, value);

// get
byte[] result = client.get(key);