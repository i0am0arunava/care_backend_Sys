import enum
from dataclasses import dataclass


class PermissionContext(enum.Enum):
    GENERIC = "GENERIC"
    FACILITY = "FACILITY"
    PATIENT = "PATIENT"
    QUESTIONNAIRE = "QUESTIONNAIRE"
    ORGANIZATION = "ORGANIZATION"
    FACILITY_ORGANIZATION = "FACILITY_ORGANIZATION"
    ENCOUNTER = "ENCOUNTER"


@dataclass
class Permission:
    """
    This class abstracts a permission
    """

    name: str
    description: str
    context: PermissionContext
    roles: list
