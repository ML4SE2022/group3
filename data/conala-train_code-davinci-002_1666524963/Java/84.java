@RequestMapping(value = "/{id}", method = RequestMethod.GET)
public String get(@PathVariable("id") String id) {
    return id;
}