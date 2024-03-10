
class State:
    """ Represents a single state in the state machine. """
    def __init__(self, name, transitions=None):
        self.name = name
        self.transitions = transitions or []

    def next_state(self, event):
        """ Determine the next state based on the given event. """
        for transition in self.transitions:
            if transition['event'] == event:
                return transition['target']
        return None

class StateMachine:
    """ A state machine implementation using the State Pattern. """
    _instance = None  # for Singleton Pattern

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(StateMachine, cls).__new__(cls)
        return cls._instance

    def __init__(self, state_chart):
        self.states = {state['name']: State(state['name'], state.get('transitions', []))
                       for state in state_chart['states']}
        self.current_state = self.states.get("S1", None)

    def send_event(self, event):
        """ Handle an event and transition to the next state if applicable. """
        if self.current_state:
            next_state_name = self.current_state.next_state(event)
            if next_state_name and next_state_name in self.states:
                self.current_state = self.states[next_state_name]
                return f"Transitioned to {next_state_name} on event '{event}'"
        return f"No transition on event '{event}' from state {self.current_state.name}"

# Assuming the rest of the functions and classes (like Validation, export_to_plantuml) remain the same.

# Note: The actual implementation might require adjustments based on the full context of the script and usage.
