public static float bytesToFloat(byte[] bytes) {
    return ByteBuffer.wrap(bytes).getFloat();
}