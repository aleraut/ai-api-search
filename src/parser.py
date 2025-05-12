import json

def load_swagger(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_endpoints(swagger_data):
    endpoints = []
    paths = swagger_data.get("paths", {})
    for path, methods in paths.items():
        for method, details in methods.items():
            description = details.get("description", "")
            endpoints.append({
                "method": method.upper(),
                "path": path,
                "description": description
            })
    return endpoints
