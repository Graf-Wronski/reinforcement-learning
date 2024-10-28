from collections.abc import Callable
from typing import Dict, Any, List

from core.problems.problem import Problem


class StaticBandit(Problem):
    def __init__(self, n_actions: int, reward_functions: List[Callable]):
        super().__init__()

        assert n_actions == len(reward_functions), \
            "Exactly one reward function per action is required."

        self.reward_functions = reward_functions
        self.n_actions = n_actions

    @property
    def _initial_state(self) -> Dict:
        return {"idx": 0}

    @staticmethod
    def transition(state: Dict, action: Any) -> Dict:
        """ Static bandits only have one state. """
        return {"idx": 0}

    @staticmethod
    def terminal(state: Dict) -> bool:
        return False

    def reward(self, state: Dict, action: Any) -> float:
        return self.reward_functions[action]()

    def allowed_actions(self, state: Dict) -> List[int]:
        return [x for x in range(self.n_actions)]
