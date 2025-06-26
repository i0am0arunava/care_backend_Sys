from typing import Any


def parse_value_field(parameter: dict[str, Any]) -> Any:
    """Extract value from different FHIR value fields."""
    value_fields = [
        "valueString",
        "valueCode",
        "valueBoolean",
        "valueCoding",
        "valueInteger",
        "valueDateTime",
    ]

    for field in value_fields:
        if field in parameter:
            return parameter[field]
    return None


def parse_extension(extension_list: list[dict[str, Any]]) -> dict[str, Any]:
    """Parse FHIR extension fields."""
    result = {}

    for extension in extension_list:
        if "url" in extension:
            if "extension" in extension:
                result[extension["url"]] = parse_extension(extension["extension"])
            else:
                for key, value in extension.items():
                    if key != "url":
                        result[extension["url"]] = value
    return result


def parse_designation_part(parts: list[dict[str, Any]]) -> dict[str, Any]:
    """Parse designation parts into a structured format."""
    designation = {}

    for part in parts:
        if "name" not in part:
            continue
        if part["name"] == "language":
            designation["language"] = parse_value_field(part)
        elif part["name"] == "use":
            designation["use"] = parse_value_field(part)
        elif part["name"] == "value":
            designation["value"] = parse_value_field(part)

    return designation


def parse_fhir_property_part(parts: list[dict[str, Any]]) -> dict[str, Any]:
    """Parse FHIR property parts into a structured format."""
    code = None
    value = None

    for part in parts:
        if part["name"] == "code":
            code = parse_value_field(part)
        elif part["name"] in ["value", "valueString"]:
            value = parse_value_field(part)

    return {code: value} if code else {}


def parse_fhir_parameter_output(parameters: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Parse FHIR parameter response into a structured format.

    Args:
        parameters: List of FHIR parameters

    Returns:
        Dict containing parsed FHIR data
    """
    response = {"properties": {}, "designations": [], "metadata": {}}

    for parameter in parameters:
        name = parameter.get("name")

        # Handle basic fields
        if name in ["code", "display", "system", "version", "name", "inactive"]:
            response["metadata"][name] = parse_value_field(parameter)

        # Handle property fields
        elif name == "property":
            property_data = parse_fhir_property_part(parameter["part"])
            for key, value in property_data.items():
                if key == "child":
                    if "children" not in response["properties"]:
                        response["properties"]["children"] = []
                    response["properties"]["children"].append(value)
                elif key == "parent":
                    if "parents" not in response["properties"]:
                        response["properties"]["parents"] = []
                    response["properties"]["parents"].append(value)
                else:
                    response["properties"][key] = value

        # Handle designation fields
        elif name == "designation":
            designation_data = {"details": parse_designation_part(parameter["part"])}
            if "extension" in parameter:
                designation_data["context"] = parse_extension(parameter["extension"])
            response["designations"].append(designation_data)
    return response
