import json
from pathlib import Path


class UnitsClient:
    _serach_cache = []
    _reverse_mapping = {}
    PAGINATION_SIZE = 100

    def create_cache(self):
        if not self._serach_cache:
            path = Path("care/emr/units/data/units.json")
            data = json.loads(path.read_bytes())
            units = data["units"]
            self._serach_cache = units
            self._reverse_mapping = {unit["code"]: unit for unit in units}

    def validate(self, value: str):
        self.create_cache()
        if value in self._reverse_mapping:
            return self._reverse_mapping[value]
        err = "Invalid Unit"
        raise ValueError(err)

    def search(self, value: str):
        self.create_cache()
        value = value.lower()
        results = []

        for unit in self._serach_cache:
            if value in unit["code"].lower() or value in unit["display"].lower():
                results.append(unit)

            if len(results) >= self.PAGINATION_SIZE:
                break

        return results


units_client = UnitsClient()
