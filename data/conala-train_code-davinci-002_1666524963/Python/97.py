def lookup(name, scope):
    if name in scope:
        return scope[name]
    elif scope.get('parent'):
        return lookup(name, scope['parent'])
    else:
        raise NameError(name)