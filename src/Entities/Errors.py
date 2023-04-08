from enum import Enum, auto

class Errors(Enum):
    SUCCESS = auto()
    FAIL = auto()
    FAILED_TO_LOCATE = auto()
    SECTION_FULL = auto()
    WRONG_PASSWORD = auto()
    MISMATCHED_PASSWORDS = auto()