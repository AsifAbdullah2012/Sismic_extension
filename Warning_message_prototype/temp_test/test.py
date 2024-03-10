import json
import sismic
from sismic.io import import_from_yaml
from sismic.io import export_to_plantuml
import yaml

# The JSON string
json_str = '''
{
    "states": [
        {"id": 1, "name": "InitialState", "transitions": [{"event": "start", "target": "OperationalState"}]},
        {"id": 2, "name": "OperationalState", "transitions": [{"event": "error", "target": "ErrorState"}, {"event": "stop", "target": "EndState"}]},
        {"id": 3, "name": "ErrorState", "transitions": [{"event": "reset", "target": "InitialState"}]},
        {"id": 4, "name": "EndState", "transitions": []}
    ]
}
'''

# Convert JSON string to Python dictionary
json_data = json.loads(json_str)

# Convert Python dictionary to YAML string
yaml_str = yaml.dump(json_data, sort_keys=False)

print(yaml_str)
