from typing import Dict

from core.agents.agent import Agent
from core.problems.problem import Problem


class Run:
    def __init__(self, problem: Problem, agent: Agent, max_steps: int):

        self.problem = problem
        self.agent = agent
        self.agent.clear_history()
        self.max_steps = max_steps
        self.n_steps = 0

    @property
    def state(self):
        return self.problem.state

    @property
    def terminal(self):
        return self.problem.terminal(self.state)

    def run(self) -> Dict:
        while self.n_steps < self.max_steps and not self.terminal:
            self.agent.act(self.problem)
            self.n_steps += 1

        steps = [n for n in range(self.n_steps)] + [None]

        # Append final state to state history.
        states = self.agent.state_history + [self.state]

        # Append 'None' values to actions and rewards, indicating final state.
        actions = self.agent.action_history + [None]
        rewards = self.agent.reward_history + [None]
        cum_rewards = self.agent.cum_rewards + [None]
        mean_rewards = self.agent.mean_rewards + [None]

        # For each state: determine whether is final state.
        is_terminal = [self.problem.terminal(state) for state in states]

        report = {
            "step": steps,
            "state": states,
            "action": actions,
            "reward": rewards,
            "cum_reward": cum_rewards,
            "mean_reward": mean_rewards,
            "is_terminal": is_terminal}

        return report
