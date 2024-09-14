def all(self, cls=None):
    """Returns a dictionary of all objects"""
    if cls is None:
        return self.__objects
    cls_name = cls.__name__
    return {key: val for key, val in self.__objects.items() if key.startswith(cls_name)}
