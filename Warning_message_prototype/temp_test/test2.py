# Assuming `states_json` is your JSON string
states_json = '''
[
    {"id": 1, "name": "S1", "transitions": [{"event": "start", "source": "","target": "S2"}]},
    {"id": 5, "name": "S2", "transitions": [{"event": "start1", "source": "S1","target": "S3"}]},
    {"id": 2, "name": "S3", "transitions": [{"event": "error", "source": "S2","target": "S4"}, {"event": "stop", "source": "S2", "target": "EndState"}]},
    {"id": 3, "name": "S4", "transitions": [{"event": "reset", "source":"S3", "target": "S1"}]},
    {"id": 4, "name": "EndState", "transitions": [{"event": "", "source": "S3","target": ""}]}
]
'''

# If you already have the JSON as a Python object, you can skip this step
import json
states = json.loads(states_json)

# New transition to be added to S1
new_transition = {"event": "new_event", "source": "S1", "target": "S5"}

# Iterate over the states to find the one with name "S1"
for state in states:
    print(state)
    if state["name"] == "S1":
        # Once found, append the new transition to the "transitions" list
        state["transitions"].append(new_transition)
        break  # Exit the loop since we've done the required operation

# If you need to convert it back to JSON
updated_states_json = json.dumps(states, indent=4)
print(updated_states_json)
