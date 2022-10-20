def remove_if(predicate, lst):
    return [x for x in lst if not predicate(x)]