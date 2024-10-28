from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict


class Result(ABC):
    def __init__(self, root: Path, overwrite: bool = False):
        """ An abstract class for result storage and loading.

        :param root: directory where result file(s) are stored.
        :param overwrite: Whether to overwrite previous results. """

        if not root.exists():
            root.mkdir(parents=True)
            print(f"Creating result dir at: \n {root} .")

        self.root = root

        # If data shall be overwritten or is not available: intialize empty.
        if overwrite or not(self.files_exist()):
            self.data = self.init_data()

        # Else: Load data from files.
        else:
            self.data = self.load()

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError("Define how many results are present. ")

    @abstractmethod
    def init_data(self) -> Any:
        raise NotImplementedError("Define how to initialise (empty) data.")

    @abstractmethod
    def load(self) -> Any:
        raise NotImplementedError("Define how to load results from disk.")

    @abstractmethod
    def store(self) -> None:
        raise NotImplementedError("Define how to store results.")

    @abstractmethod
    def files_exist(self) -> bool:
        raise NotImplementedError("Define how to assert file integrity.")

    def add_result(self, result_as_dict: Dict, store_it: bool = True) -> None:
        """ Adds result to current data and (optionally) stores it.

        :param result_as_dict: The next result to add.
        :param store_it: Storage desired? """

        self.data = self._add_result(self.data, result_as_dict)

        if store_it:
            self.store()

    @staticmethod
    def _add_result(data: Any, result_as_dict: Dict) -> Any:
        raise NotImplementedError("Define how results are merged into data.")