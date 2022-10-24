@RequestMapping(value = "/", method = RequestMethod.GET)
public ResponseEntity<String> get() {
    HttpHeaders headers = new HttpHeaders();
    headers.add("Content-Type", "application/json; charset=utf-8");
    return new ResponseEntity<String>("{\"message\": \"Hello World\"}", headers, HttpStatus.OK);
}