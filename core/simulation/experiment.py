from typing import List

import numpy as np
import random

from core.agents.agent import Agent
from core.problems.problem import Problem
from core.simulation.results.result import Result
from core.simulation.run import Run


class Experiment:

    def __init__(self, result_object: Result):
        self.result_object = result_object

    def __str__(self) -> str:
        raise NotImplementedError("Define the experiments name.")

    @staticmethod
    def _seed(seed: int) -> None:
        np.random.seed(seed)
        random.seed(seed)

    @property
    def problem(self) -> Problem:
        raise NotImplementedError("Define the problem at hand.")

    @property
    def agents(self) -> List[Agent]:
        raise NotImplementedError("Define the agent constructors.")

    @property
    def seeds(self) -> List[int]:
        raise NotImplementedError("Define the seeds.")

    @property
    def runs_per_seed(self) -> int:
        raise NotImplementedError("Define how many runs per seed.")

    @property
    def steps_per_run(self) -> int:
        """ Overwrite this property, if you want another number. """
        return 1000

    def run(self):
        for seed in self.seeds:
            print(f"Seed: {seed}")
            self._seed(seed)
            problem = self.problem  # Make problem constant for seed.

            for agent in self.agents:
                print(f"Agent: {str(agent)}")
                for run_idx in range(self.runs_per_seed):
                    if run_idx == 0 or (run_idx + 1) % 100 == 0:
                        print(f"Run: {run_idx + 1} / {self.runs_per_seed}.")
                        run = Run(problem, agent, max_steps=self.steps_per_run)
                        report = run.run()
                        report["seed"] = seed
                        report["agent"] = str(agent)
                        report["run"] = run_idx
                        self.result_object.add_result(report)
