import requests


class FHIRClient:
    """
    This client will be used for all queries performed over the FHIR protocol
    This class is designed to perform FHIR based queries to some remote server and convert them into python objects
    """

    def __init__(self, server_url):
        self.server_url = server_url

    def query(self, *, method, resource, operation=None, parameters, detail=None):
        url = f"{self.server_url}/{resource}"
        if detail:
            url += f"/{detail}"
        if operation:
            url += f"/${operation}"
        request_kwargs = {}
        if method == "GET":
            request_kwargs["params"] = parameters
        else:
            request_kwargs["json"] = parameters
        response = requests.request(method, url, **request_kwargs, timeout=60)
        return response.json()
