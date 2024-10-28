from pathlib import Path
from typing import Dict

import pandas as pd

from core.simulation.results.result import Result


class PandasTable(Result):
    def __init__(self, root: Path, overwrite: bool = False):
        super().__init__(root, overwrite)

    def __len__(self) -> int:
        return len(self.data)

    @property
    def csv_path(self) -> Path:
        return self.root / "result_table.csv"

    def init_data(self) -> pd.DataFrame:
        return pd.DataFrame({})

    def load(self) -> pd.DataFrame:
        return pd.read_csv(self.csv_path)

    def store(self) -> None:
        self.data.to_csv(self.csv_path, index=False)

    def files_exist(self) -> bool:
        return self.csv_path.exists()

    @staticmethod
    def _add_result(data: pd.DataFrame, result_as_dict: Dict) -> pd.DataFrame:
        """ Merge a new result with the current table. """

        # Convert new result to DataFrame.
        result_as_frame = pd.DataFrame(result_as_dict)

        # If it is first result, simply return it.
        if len(data) == 0:
            return result_as_frame

        # Else: assert column integrity and merge.
        assert list(data.columns) == list(result_as_frame.columns)
        return pd.concat([data, result_as_frame], ignore_index=True)