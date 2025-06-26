from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from care.emr.api.viewsets.base import EMRModelViewSet, EMRQuestionnaireResponseMixin
from care.emr.api.viewsets.encounter_authz_base import EncounterBasedAuthorizationBase
from care.emr.models.medication_administration import MedicationAdministration
from care.emr.registries.system_questionnaire.system_questionnaire import (
    InternalQuestionnaireRegistry,
)
from care.emr.resources.medication.administration.spec import (
    MedicationAdministrationReadSpec,
    MedicationAdministrationSpec,
    MedicationAdministrationUpdateSpec,
)
from care.emr.resources.questionnaire.spec import SubjectType
from care.utils.filters.multiselect import MultiSelectFilter


class MedicationAdministrationFilter(filters.FilterSet):
    encounter = filters.UUIDFilter(field_name="encounter__external_id")
    request = filters.UUIDFilter(field_name="request__external_id")
    occurrence_period_start = filters.DateTimeFromToRangeFilter()
    occurrence_period_end = filters.DateTimeFromToRangeFilter()
    status = MultiSelectFilter(field_name="status")


class MedicationAdministrationViewSet(
    EncounterBasedAuthorizationBase, EMRQuestionnaireResponseMixin, EMRModelViewSet
):
    database_model = MedicationAdministration
    pydantic_model = MedicationAdministrationSpec
    pydantic_update_model = MedicationAdministrationUpdateSpec
    pydantic_read_model = MedicationAdministrationReadSpec
    questionnaire_type = "medication_administration"
    questionnaire_title = "Medication Administration"
    questionnaire_description = "Medication Administration"
    questionnaire_subject_type = SubjectType.patient.value
    filterset_class = MedicationAdministrationFilter
    filter_backends = [
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    ]
    ordering_fields = ["created_date", "modified_date"]

    def get_queryset(self):
        self.authorize_read_encounter()
        return (
            super()
            .get_queryset()
            .filter(patient__external_id=self.kwargs["patient_external_id"])
            .select_related("patient", "encounter", "created_by", "updated_by")
        )


InternalQuestionnaireRegistry.register(MedicationAdministrationViewSet)
