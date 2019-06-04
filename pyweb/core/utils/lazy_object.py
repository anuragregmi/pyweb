
class LazyObject(object):
    """
    A wrapper for another class that can be used to delay instantiation of the
    wrapped class.

    An implementation of singleton object with lazy instantiation.
    """

    instance = None

    def setup(self, *args, **kwargs):
        """
        setup function

        function called to instantiate the wrapped object. Assign the object to
        the `instance` attribute.
        """
        raise NotImplementedError

    def __init__(self):
        """
        set instance to None
        """
        self.instance = None

    def __getattr__(self, item):
        if self.instance is None:
            self.setup()
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        if key == 'instance':
            # Assign to __dict__ to avoid infinite __setattr__ loops.
            self.__dict__['instance'] = value
        else:
            if self.instance is None:
                self.setup()
            setattr(self.instance, key, value)
