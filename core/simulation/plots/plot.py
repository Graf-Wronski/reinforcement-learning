from abc import ABC
from typing import Dict, Optional
import seaborn as sns
from matplotlib import pyplot as plt

from core.simulation.results.result import Result
from core.utils.file import valid_filename


class Plot(ABC):
    def __init__(self, result: Result, fig_title: str = None):
        self._save_name = fig_title
        self.root = result.root
        self.data = result.data

    def __str__(self) -> Optional[str]:
        return self._save_name


class ScatterPlot(Plot):
    def __init__(self, result: Result, save_name: Optional[str] = None):
        super().__init__(result, save_name)

    @property
    def x(self) -> str:
        raise NotImplementedError("Define x-axis data.")

    @property
    def y(self) -> str:
        raise NotImplementedError("Define y-axis data.")

    @property
    def plot_kwargs(self) -> Dict:
        return {}

    @property
    def figure_kwargs(self) -> Dict:
        return {}

    def plot(self, show: bool = False, save: bool = True) -> plt.Figure:

        _, ax = plt.subplots()

        fig = sns.scatterplot(
            self.data,
            x=self.x, y=self.y,
            ax=ax,
            **self.plot_kwargs)

        plt.title(str(self))

        if save:
            png_path = self.root / f"{valid_filename(str(self))}.png"
            plt.savefig(png_path, **self.figure_kwargs)

        if show:
            plt.show()

        return fig


class LinePlot(Plot):
    def __init__(self, result: Result, save_name: Optional[str] = None):
        super().__init__(result, save_name)

    @property
    def x(self) -> str:
        raise NotImplementedError("Define x-axis data.")

    @property
    def y(self) -> str:
        raise NotImplementedError("Define y-axis data.")

    @property
    def plot_kwargs(self) -> Dict:
        return {}

    @property
    def figure_kwargs(self) -> Dict:
        return {}

    def plot(self, show: bool = False, save: bool = True) -> plt.Figure:

        _, ax = plt.subplots()

        fig = sns.lineplot(
            self.data,
            ax=ax,
            x=self.x, y=self.y,
            **self.plot_kwargs)

        plt.title(str(self))

        if show:
            plt.show()

        if save:
            png_path = self.root / f"{valid_filename(str(self))}.png"
            plt.savefig(png_path, **self.figure_kwargs)

        return fig
