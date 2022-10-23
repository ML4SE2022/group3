public class Book {
    private String name;
    private List<Author> authors;
}

public class Author {
    private String name;
    private List<Book> books;
}

public class BookRepository {
    public List<Book> findByAuthors(List<Author> authors) {
        // TODO
    }
}