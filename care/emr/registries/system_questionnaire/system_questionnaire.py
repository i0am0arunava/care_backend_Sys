import uuid

from care.emr.resources.questionnaire.spec import QuestionnaireStatus


class InternalQuestionnaireRegistry:
    _questionnaires = {}

    @classmethod
    def register(cls, view) -> None:
        cls._questionnaires[view.questionnaire_type] = view

    @classmethod
    def serialize(cls, view):
        return {
            "version": "1.0",
            "id": str(uuid.uuid4()),
            "title": view.questionnaire_title,
            "description": view.questionnaire_description,
            "slug": view.questionnaire_type,
            "type": view.questionnaire_type,
            "status": QuestionnaireStatus.active.value,
            "subject_type": view.questionnaire_subject_type,
        }

    @classmethod
    def search_questionnaire(cls, term):
        return [
            cls.serialize(cls._questionnaires[view])
            for view in cls._questionnaires
            if term in view
        ]

    @classmethod
    def check_type_exists(cls, questionnaire_type):
        return questionnaire_type in cls._questionnaires
