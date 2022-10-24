public class Hierarchy {
    private final Map<String, List<String>> hierarchy;

    public Hierarchy(Map<String, List<String>> hierarchy) {
        this.hierarchy = hierarchy;
    }

    public List<String> getChildren(String parent) {
        return hierarchy.get(parent);
    }

    public List<String> getParents(String child) {
        return hierarchy.entrySet().stream()
                .filter(entry -> entry.getValue().contains(child))
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());
    }

    public List<String> getAncestors(String child) {
        List<String> ancestors = new ArrayList<>();
        List<String> parents = getParents(child);
        ancestors.addAll(parents);
        parents.forEach(parent -> ancestors.addAll(getAncestors(parent)));
        return ancestors;
    }

    public List<String> getDescendants(String parent) {
        List<String> descendants = new ArrayList<>();
        List<String> children = getChildren(parent);
        descendants.addAll(children);
        children.forEach(child -> descendants.addAll(getDescendants(child)));
        return descendants;
    }
}