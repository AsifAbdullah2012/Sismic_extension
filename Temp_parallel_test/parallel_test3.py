from sismic.io import import_from_yaml, export_to_plantuml
from sismic.model import Statechart, Transition
from sismic.interpreter import Interpreter
from sismic.model import Statechart, Transition, CompoundState, BasicState, FinalState
from extend import extend
import asyncio



elevator = import_from_yaml(filepath='sismic/docs/examples/elevator/elevator.yaml')
print(elevator._parent)


# Create an interpreter for this statechart
interpreter = Interpreter(elevator)

active_state_before_execution = interpreter.configuration

step = interpreter.execute_once()

active_state_after_execution = interpreter.configuration

all_events_for_the_current_state = elevator.events_for(interpreter.configuration)

plantuml_data = export_to_plantuml(elevator)
with open('Elevator_statechart.plantuml', 'w') as file:
    file.write(plantuml_data)