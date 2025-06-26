from pydantic import UUID4

from care.emr.models import QuestionnaireOrganization
from care.emr.resources.base import EMRResource


class QuestionnaireOrganizationBaseSpec(EMRResource):
    __model__ = QuestionnaireOrganization
    __exclude__ = ["questionnaire", "organization"]


class QuestionnaireOrganziationWriteSpec(QuestionnaireOrganizationBaseSpec):
    organization: UUID4


class QuestionnaireOrganizationReadSpec(QuestionnaireOrganizationBaseSpec):
    organization: dict
