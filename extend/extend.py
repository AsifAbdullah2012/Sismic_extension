import abc

from time import time
from sismic.model import Statechart
from sismic.model.elements import (CompositeStateMixin, CompoundState, HistoryStateMixin,
                       StateMixin, Transition, TransitionStateMixin)

from typing import Callable, Dict, Iterable, List, Optional, Union, cast

__all__ = ['Change', 'StateChange', 'TransitionChange']

class Change(metaclass=abc.ABCMeta):
    """
    Abstract implementation of a change.
    contains two abstract method add and remove

    """
    @abc.abstractproperty
    def add(self) -> float:
        """
        adding states / transitions
        """
        raise NotImplementedError()
    
    @abc.abstractproperty
    def remove(self) -> float:
        """
        removing states / transitions
        """
        raise NotImplementedError()

    def __repr__(self):
        return '{}[{}]'.format(self.__class__.__name__, self.time)
    

class StateChange(Change):
    def __init__(self, statechart, interpreter) -> None:
        self.SC = statechart
        self.interpreter = interpreter

    def add(self, state: StateMixin, parent: str):
        self.SC.add_state(state, parent)

    def remove(self, statename: str):
        self.SC.remove_state(statename)

class TransitionChange(Change):
    def __init__(self, statechart, interpreter) -> None:
        self.SC = statechart
        self.interpreter = interpreter

    def add(self, transition: Transition): 
        self.SC.add_transition(transition)
    def remove(self, transition: Transition):
        self.SC.remove_transition(transition)

    
