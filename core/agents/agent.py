from typing import List, Dict

from core.problems.problem import Problem


class Agent:
    def __init__(self):
        self.state_history = []
        self.action_history = []
        self.reward_history = []
        self.cum_rewards = []
        self.mean_rewards = []

    def clear_history(self):
        self.state_history = []
        self.action_history = []
        self.reward_history = []
        self.cum_rewards = []
        self.mean_rewards = []

    def __str__(self):
        raise NotImplementedError("Define the agents name.")

    @property
    def step_size(self) -> float:
        """ 1 / n as default step_size. """
        return 1 / self.n_step

    @property
    def n_step(self) -> int:
        return len(self.state_history)

    def act(self, problem: Problem) -> None:
        """ Choose an action and execute it."""

        current_state = problem.state
        available_actions = problem.allowed_actions(current_state)
        action = self.strategy(current_state, available_actions)
        reward = problem.apply(action)
        self.log(action, current_state, reward)

    def log(self, action: int, state: Dict, reward: float) -> None:
        """ Log an action and its effects. """

        self.action_history.append(action)
        self.state_history.append(state)
        self.reward_history.append(reward)

        # If rewards empty: Add 0.0 to current reward. Else: old cummulative.
        old_cum = self.cum_rewards[-1] if len(self.cum_rewards) > 0 else 0.0
        new_cum = reward + old_cum
        self.cum_rewards.append(new_cum)
        self.mean_rewards.append(new_cum / self.n_step)

    def strategy(self, state: Dict, actions: List[int]) -> int:
        raise NotImplementedError("Define actions based on state, action"
                                  "and reward history.")

