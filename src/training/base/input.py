"""Base input class for various data sources."""

from abc import ABC, abstractmethod


class BaseInput(ABC):
    """Abstract base class for input data handling."""

    @abstractmethod
    def load_data(self, source):
        """Load data from the specified source."""
        pass
