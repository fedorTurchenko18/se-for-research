"""Base class for various output plots formats."""

from abc import ABC, abstractmethod


class BaseOutput(ABC):
    """Abstract base class for output data handling."""

    @abstractmethod
    def save_output(self, fig, destination):
        """Save output data to the specified destination."""
        pass
