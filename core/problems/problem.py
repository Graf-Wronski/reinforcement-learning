from abc import ABC
from typing import Dict, List, Any


class Problem(ABC):
    def __init__(self):
        self._state = self._initial_state

    @property
    def _initial_state(self) -> Dict:
        raise NotImplementedError("Defines the initial problem state.")

    @property
    def state(self) -> Dict:
        return self._state

    def apply(self, action: Any) -> float:
        """ Execute an action.

        :param action: An action to be applied to the current state.
        :return: The reward calculated based on the current state and
            given action. """

        reward = self.reward(self._state, action)
        self._state = self.transition(self._state, action)
        return reward

    @staticmethod
    def transition(state: Dict, action: Any) -> Dict:
        raise NotImplementedError("Describe state transitions.")

    @staticmethod
    def terminal(state: Dict) -> bool:
        raise NotImplementedError("Defines which states are terminal. ")

    def reward(self, state: Dict, action: Any) -> float:
        raise NotImplementedError("Defines reward based on action and state.")

    def allowed_actions(self, state: Dict) -> List:
        raise NotImplementedError("Define the allowed actions for each state.")