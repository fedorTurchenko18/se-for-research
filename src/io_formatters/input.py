"""Input formatters for various data sources."""

import pandas as pd
from src.training.base.input import BaseInput

class CSVReader(BaseInput):
    """Class to read and process CSV input data."""

    def load_data(self, source):
        """Load data from a CSV file."""
        try:
            data = pd.read_csv(source)
            return data
        except Exception as e:
            raise IOError(f"Error reading CSV file at {source}: {e}")


class JSONReader(BaseInput):
    """Class to read and process JSON input data."""

    def load_data(self, source, orient='records', lines=True):
        """Load data from a JSON file."""
        try:
            data = pd.read_json(source, orient=orient, lines=lines)
            return data
        except Exception as e:
            raise IOError(f"Error reading JSON file at {source}: {e}")


class ExcelReader(BaseInput):
    """Class to read and process Excel input data."""

    def load_data(self, source):
        """Load data from an Excel file."""
        try:
            data = pd.read_excel(source)
            return data
        except Exception as e:
            raise IOError(f"Error reading Excel file at {source}: {e}")
