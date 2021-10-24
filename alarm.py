from __future__ import annotations
from abc import ABC, abstractmethod


class Alarm:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self) -> None:
        self.transition_to(Off())

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        # print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def reset(self):
        self._state.reset()

    def activate(self):
        self._state.activate()

    def deactivate(self):
        self._state.deactivate()

    def motionDetected(self):
        self._state.motionDetected()

    def isActive(self):
        return self._state.isActive()

    def isRinging(self):
        return self._state.isRinging()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> Alarm:
        return self._context

    @context.setter
    def context(self, context: Alarm) -> None:
        self._context = context

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def activate(self) -> None:
        pass

    @abstractmethod
    def deactivate(self) -> None:
        pass

    @abstractmethod
    def motionDetected(self) -> None:
        pass

    @abstractmethod
    def isActive(self) -> None:
        pass

    @abstractmethod
    def isRinging(self) -> None:
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""


class Off(State):
    def reset(self) -> None:
        pass

    def activate(self) -> None:
        self.context.transition_to(On())

    def deactivate(self) -> None:
        pass

    def motionDetected(self) -> None:
        pass

    def isActive(self):
        return False

    def isRinging(self):
        return False


class On(State):
    def reset(self) -> None:
        pass

    def activate(self) -> None:
        pass

    def deactivate(self) -> None:
        self.context.transition_to(Off())

    def motionDetected(self) -> None:
        self.context.transition_to(Ringing())

    def isActive(self):
        return True

    def isRinging(self):
        return False

class Ringing(State):
    def reset(self) -> None:
        self.context.transition_to(On())

    def activate(self) -> None:
        pass

    def deactivate(self) -> None:
        self.context.transition_to(Off())

    def motionDetected(self) -> None:
        pass

    def isActive(self):
        return True

    def isRinging(self):
        return True