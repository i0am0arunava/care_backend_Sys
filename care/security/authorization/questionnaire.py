from care.emr.models.organization import OrganizationUser
from care.security.authorization.base import (
    AuthorizationController,
    AuthorizationHandler,
)
from care.security.permissions.questionnaire import QuestionnairePermissions


class QuestionnaireAccess(AuthorizationHandler):
    def can_read_questionnaire(self, user, org=None):
        return self.check_permission_in_organization(
            [QuestionnairePermissions.can_read_questionnaire.name], user, org
        )

    def can_write_questionnaire(self, user, org=None):
        if org:
            org = [org]
        return self.check_permission_in_organization(
            [QuestionnairePermissions.can_write_questionnaire.name], user, org
        )

    def can_write_questionnaire_obj(self, user, questionnaire):
        return self.check_permission_in_organization(
            [QuestionnairePermissions.can_write_questionnaire.name],
            user,
            questionnaire.organization_cache,
        )

    def can_submit_questionnaire_obj(self, user, questionnaire):
        return self.check_permission_in_organization(
            [QuestionnairePermissions.can_submit_questionnaire.name],
            user,
            questionnaire.organization_cache,
        )

    def get_filtered_questionnaires(self, qs, user):
        if user.is_superuser:
            return qs
        roles = self.get_role_from_permissions(
            [QuestionnairePermissions.can_read_questionnaire.name]
        )
        organization_ids = list(
            OrganizationUser.objects.filter(user=user, role_id__in=roles).values_list(
                "organization_id", flat=True
            )
        )
        return qs.filter(organization_cache__overlap=organization_ids)


AuthorizationController.register_internal_controller(QuestionnaireAccess)
