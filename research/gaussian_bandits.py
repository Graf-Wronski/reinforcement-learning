from collections.abc import Callable
from pathlib import Path
from typing import List, Dict

import numpy as np

from core.agents.agent import Agent
from core.agents.epsilon_greedy import EpsilonGreedy
from core.simulation.experiment import Experiment
from core.problems.problem import Problem
from core.problems.static_bandit import StaticBandit
from core.simulation.plots.plot import LinePlot
from core.simulation.results.pandas_table import PandasTable


def gaussian_reward(loc: float, variance: float) -> Callable:
    return lambda: np.round(np.random.normal(loc, variance), 4)

class GaussianBanditExperiment(Experiment):
    def __str__(self):
        return "gaussian_bandit_experiment"

    @property
    def problem(self) -> Problem:
        locs = np.random.normal(loc=0, scale=1 , size=10)
        reward_functions = [gaussian_reward(loc, variance=1.0) for loc in locs]
        problem = StaticBandit(n_actions=10, reward_functions=reward_functions)
        return problem

    @property
    def agents(self) -> List[Agent]:
        epsilons = [np.round(0.015 * n, 5) for n in range(7)]
        agents = [EpsilonGreedy(epsilon=eps) for eps in epsilons]
        return agents

    @property
    def steps_per_run(self) -> int:
        return 5_000

    @property
    def seeds(self) -> List[int]:
        return [3, 5, 17]

    @property
    def runs_per_seed(self) -> int:
        return 100


class MeanRewardPlot(LinePlot):
    def __init__(self, experiment: Experiment):
        fig_title = "Mean Reward"
        super().__init__(experiment.result_object, fig_title)

    @property
    def x(self) -> str:
        return "step"

    @property
    def y(self) -> str:
        return "mean_reward"

    @property
    def plot_kwargs(self) -> Dict:
        return {"hue": "agent", "errorbar": None}


class CummulativeRewardPlot(LinePlot):
    def __init__(self, experiment: Experiment):
        fig_title = "Cummulative Rewards"
        super().__init__(experiment.result_object, fig_title)

    @property
    def x(self) -> str:
        return "step"

    @property
    def y(self) -> str:
        return "cum_reward"

    @property
    def plot_kwargs(self) -> Dict:
        return {"hue": "agent", "errorbar": None}


if __name__ == "__main__":
    path = Path(".") / "results"
    result_table = PandasTable(root=path, overwrite=True)
    exp = GaussianBanditExperiment(result_object=result_table)
    exp.run()
    _ = MeanRewardPlot(experiment=exp).plot(show=False)
    _ = CummulativeRewardPlot(experiment=exp).plot(show=False)