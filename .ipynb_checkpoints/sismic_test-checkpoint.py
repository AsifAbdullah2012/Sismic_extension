from sismic.io import import_from_yaml
from sismic.interpreter import Interpreter

# Load statechart from yaml file
elevator = import_from_yaml(filepath='examples/elevator/elevator.yaml')

