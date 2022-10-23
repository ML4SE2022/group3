public class User {
    @Id
    private String id;
    @Required
    private String name;
    @Required
    private String email;
    @Required
    private String password;
    @Required
    private String role;
    @Required
    private String status;
    @Required
    private String createdAt;
    @Required
    private String updatedAt;
}