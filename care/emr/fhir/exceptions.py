class BaseFHIRError(Exception):
    pass


class MoreThanOneFHIRResourceFoundError(BaseFHIRError):
    pass
