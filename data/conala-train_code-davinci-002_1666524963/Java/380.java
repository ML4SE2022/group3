@DELETE
@Path("/{id}")
public Response delete(@PathParam("id") int id) {
    try {
        User user = userService.findById(id);
        userService.delete(user);
        return Response.status(Response.Status.OK).build();
    } catch (Exception e) {
        return Response.status(Response.Status.NOT_FOUND).build();
    }
}