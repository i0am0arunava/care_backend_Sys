import datetime
from enum import Enum

from django.utils.timezone import is_aware, make_aware
from pydantic import UUID4, field_validator
from rest_framework.generics import get_object_or_404

from care.emr.models.condition import Condition
from care.emr.models.encounter import Encounter
from care.emr.resources.base import EMRResource
from care.emr.resources.common.coding import Coding
from care.emr.resources.condition.valueset import CARE_CODITION_CODE_VALUESET
from care.emr.resources.user.spec import UserSpec
from care.emr.utils.valueset_coding_type import ValueSetBoundCoding
from care.utils.time_util import care_now


class ClinicalStatusChoices(str, Enum):
    active = "active"
    recurrence = "recurrence"
    relapse = "relapse"
    inactive = "inactive"
    remission = "remission"
    resolved = "resolved"
    unknown = "unknown"


class VerificationStatusChoices(str, Enum):
    unconfirmed = "unconfirmed"
    provisional = "provisional"
    differential = "differential"
    confirmed = "confirmed"
    refuted = "refuted"
    entered_in_error = "entered_in_error"


class CategoryChoices(str, Enum):
    problem_list_item = "problem_list_item"
    encounter_diagnosis = "encounter_diagnosis"
    chronic_condition = "chronic_condition"


class SeverityChoices(str, Enum):
    mild = "mild"
    moderate = "moderate"
    severe = "severe"


class ConditionOnSetSpec(EMRResource):
    onset_datetime: datetime.datetime | None = None
    onset_age: int | None = None
    onset_string: str | None = None
    note: str | None = None

    @field_validator("onset_datetime")
    @classmethod
    def validate_onset_datetime(cls, onset_datetime: datetime.datetime, info):
        if onset_datetime:
            if not is_aware(onset_datetime):
                onset_datetime = make_aware(onset_datetime)
            if onset_datetime > care_now():
                raise ValueError("Onset date cannot be in the future")
        return onset_datetime


class ConditionAbatementSpec(EMRResource):
    abatement_datetime: datetime.datetime | None = None
    abatement_age: int | None = None
    abatement_string: str | None = None
    note: str | None = None


class BaseConditionSpec(EMRResource):
    __model__ = Condition
    __exclude__ = ["patient", "encounter"]
    id: UUID4 = None


class ConditionSpec(BaseConditionSpec):
    clinical_status: ClinicalStatusChoices | None = None
    verification_status: VerificationStatusChoices
    severity: SeverityChoices | None = None
    code: ValueSetBoundCoding[CARE_CODITION_CODE_VALUESET.slug]
    encounter: UUID4
    onset: ConditionOnSetSpec = {}
    abatement: ConditionAbatementSpec = {}
    note: str | None = None
    category: CategoryChoices

    @field_validator("encounter")
    @classmethod
    def validate_encounter_exists(cls, encounter):
        if not Encounter.objects.filter(external_id=encounter).exists():
            err = "Encounter not found"
            raise ValueError(err)
        return encounter

    def perform_extra_deserialization(self, is_update, obj):
        if not is_update:
            obj.encounter = Encounter.objects.get(
                external_id=self.encounter
            )  # Needs more validation
            obj.patient = obj.encounter.patient


class ConditionReadSpec(BaseConditionSpec):
    """
    Validation for deeper models may not be required on read, Just an extra optimisation
    """

    # Maybe we can use model_construct() to be better at reads, need profiling to be absolutely sure

    clinical_status: str
    verification_status: str
    category: str
    criticality: str
    severity: str
    code: Coding
    encounter: UUID4
    onset: ConditionOnSetSpec = dict
    abatement: ConditionAbatementSpec = dict
    created_by: UserSpec = dict
    updated_by: UserSpec = dict
    note: str | None = None
    created_date: datetime.datetime
    modified_date: datetime.datetime

    @classmethod
    def perform_extra_serialization(cls, mapping, obj):
        mapping["id"] = obj.external_id
        if obj.encounter:
            mapping["encounter"] = obj.encounter.external_id

        if obj.created_by:
            mapping["created_by"] = UserSpec.serialize(obj.created_by)
        if obj.updated_by:
            mapping["updated_by"] = UserSpec.serialize(obj.updated_by)


class ConditionUpdateSpec(BaseConditionSpec):
    clinical_status: ClinicalStatusChoices | None = None
    verification_status: VerificationStatusChoices
    severity: SeverityChoices | None = None
    code: ValueSetBoundCoding[CARE_CODITION_CODE_VALUESET.slug]
    onset: ConditionOnSetSpec = {}
    abatement: ConditionAbatementSpec = {}
    note: str | None = None


class ChronicConditionUpdateSpec(ConditionUpdateSpec):
    encounter: UUID4

    def perform_extra_deserialization(self, is_update, obj):
        if self.encounter:
            obj.encounter = get_object_or_404(Encounter, external_id=self.encounter)
