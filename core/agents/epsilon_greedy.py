from typing import Dict, List

import numpy as np

from core.agents.agent import Agent


class EpsilonGreedy(Agent):
    def __init__(self, epsilon: float, default_reward: float = - 1.0):
        super().__init__()
        self.epsilon = epsilon
        self.default_reward = default_reward

    def __str__(self) -> str:
        return f"epsilon_greedy_{self.epsilon}".replace(".", "_")

    def expected_reward(self, state, action: int) -> float:
        """ Q* function describing the expected reward (=value).

        :param state:
        :param action:
        :return:
        """
        # If state was never visited, we return default reward.
        if state not in self.state_history:
            return self.default_reward

        # Else we check what to expect from action in this state.
        else:
            # Get actions and rewards corresponding to state.
            indices = self.state_history.index(state)
            actions = self.state_history[indices]
            rewards = self.reward_history[indices]

            # If action was never executed, return default reward.
            if action not in actions:
                return self.default_reward

            # Else return mean over previous rewards.
            else:
                return np.mean(rewards[actions.index(action)])

    def strategy(self, state: Dict, actions: List[int]) -> int:
        """ Epsilon-greedy strategy.

        :param state: Current state.
        :param actions: Possible actions.
        :return: The selected actions. """

        # With probability epsilon: return a random action.
        if np.random.rand() < self.epsilon:
            return np.random.choice(actions)
        # Else choose a random expectation maximising action (greedy).
        else:
            expected_rewards = [self.expected_reward(state, action)
                                for action in actions]
            max_val = np.max(expected_rewards)
            max_indices =  np.argwhere(expected_rewards == max_val)
            return actions[np.random.choice(max_indices.flatten())]
