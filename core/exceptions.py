class UniqueUserError(BaseException):

    def __init__(self, msg, *args: object) -> None:
        super().__init__(msg)
