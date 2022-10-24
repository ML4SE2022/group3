public static int[] hex2Rgb(String colorStr) {
    return new int[]{
            Integer.valueOf( colorStr.substring( 1, 3 ), 16 ),
            Integer.valueOf( colorStr.substring( 3, 5 ), 16 ),
            Integer.valueOf( colorStr.substring( 5, 7 ), 16 ) };
}

public static String rgb2Hex(int[] rgb) {
    return String.format("#%02x%02x%02x", rgb[0], rgb[1], rgb[2]);
}