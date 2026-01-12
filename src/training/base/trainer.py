"""Abstraction for machine learning trainers."""

from abc import ABC, abstractmethod

class Trainer(ABC):
    """Abstract base class for machine learning trainers."""

    @abstractmethod
    def featurize(self, data):
        """Extract features from the provided data."""
        pass

    @abstractmethod
    def train(self, X, y):
        """Train the model with the provided data."""
        pass

    @abstractmethod
    def evaluate(self, y_pred, y_true):
        """Evaluate the model with the provided data."""
        pass

    @abstractmethod
    def predict(self, X):
        """Make predictions using the trained model."""
        pass

    @abstractmethod
    def save_model(self, path):
        """Save the trained model to the specified path."""
        pass

    @abstractmethod
    def load_model(self, path):
        """Load a trained model from the specified path."""
        pass
