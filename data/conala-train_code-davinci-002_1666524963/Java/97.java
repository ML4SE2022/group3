public class Scope {
    private Map<String, Object> attributes = new HashMap<>();

    public void setAttribute(String name, Object value) {
        attributes.put(name, value);
    }

    public Object getAttribute(String name) {
        return attributes.get(name);
    }
}

public class ScopeHierarchy {
    private Scope root;

    public ScopeHierarchy(Scope root) {
        this.root = root;
    }

    public Object lookup(String name) {
        Scope current = root;
        while (current != null) {
            Object value = current.getAttribute(name);
            if (value != null) {
                return value;
            }
            current = current.getParent();
        }
        return null;
    }
}