class UniqueUserError(BaseException):
    """
    Exception class for unique password & username check

    :param BaseException
    """

    def __init__(self, msg) -> None:
        super(UniqueUserError, self).__init__(msg)
