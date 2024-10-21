class MyClass:
    """A simple class with a single attribute.

    :param x: An integer parameter.
    """
    x: str

    def __init__(self, x: int):
        self.x = str(x)
