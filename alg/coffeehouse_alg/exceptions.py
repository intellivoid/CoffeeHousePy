__all__ = ["CoffeeHouseAlgException"]


class CoffeeHouseAlgException(Exception):
    """
    Exception raised by API errors.
    The exception message is set to the server's response.
    """

    def __init__(self, type, message, content):
        self.type = type
        self.content = content
        self.message = "{0} ERROR: {1}".format(type, message)
        super().__init__(self.message or content)
