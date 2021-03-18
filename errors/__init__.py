class ParsingError(Exception):
    """
    This exception is raised whenever there's an error in parsing the graphql sdl provided to the parser
    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)
