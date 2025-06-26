# ruff : noqa : N815

from pydantic.main import BaseModel

from care.emr.fhir.exceptions import MoreThanOneFHIRResourceFoundError
from care.emr.fhir.resources.base import ResourceManger
from care.facility.models import User

User.objects.filter()


class CodeSystemResource(ResourceManger):
    allowed_properties = ["name", "url"]
    resource = "CodeSystem"

    def serialize(self, result):
        return CodeSystem(
            name=result["resource"]["name"],
            resourceType=result["resource"]["resourceType"],
            id=result["resource"]["id"],
            url=result["resource"]["url"],
            title=result["resource"]["title"],
        )

    def search(self):
        full_result = self.query("GET", self.resource, self._filters)
        results = full_result["entry"]
        return self.handle_list(results)

    def get(self):
        full_result = self.query("GET", self.resource, self._filters)
        if full_result["total"] != 1:
            raise MoreThanOneFHIRResourceFoundError
        results = full_result["entry"]
        return self.serialize(results[0])


class CodeSystem(BaseModel):
    name: str
    resourceType: str
    id: str
    url: str
    title: str
