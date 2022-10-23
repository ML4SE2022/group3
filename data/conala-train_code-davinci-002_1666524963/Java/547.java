List<User> users = new Select()
    .from(User.class)
    .join(Profile.class)
    .on("user.profile_id = profile.id")
    .orderBy("profile.name")
    .execute();