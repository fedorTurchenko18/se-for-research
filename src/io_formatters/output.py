"""Output formatters for various graphics formats."""

from src.training.base.output import BaseOutput
import matplotlib
import matplotlib.figure
import os
import warnings


class ImageWriter(BaseOutput):
    """Class to save output plots in PNG format."""

    def save_output(self, fig: matplotlib.figure.Figure, destination, format="png"):
        """Save the plot as a PNG file."""
        # Ensure destination directory exists
        os.makedirs(
            os.path.dirname(destination) if os.path.dirname(destination) else ".",
            exist_ok=True,
        )
        fig.savefig(destination, format=format)


class LatexWriter(BaseOutput):
    """Class to save output plots in LaTeX code format."""

    def __init__(self):
        """Initialize LatexWriter with optional tikzplotlib dependency check."""
        try:
            import tikzplotlib

            self._tikzplotlib = tikzplotlib
        except ImportError:
            warnings.warn(
                "tikzplotlib not found. Install it with 'pip install tikzplotlib'"
                " for LaTeX code generation functionality.",
                UserWarning,
            )
            self._tikzplotlib = None

    def save_output(
        self,
        fig: matplotlib.figure.Figure,
        destination: str,
        standalone: bool = False,
        extra_axis_parameters=None,
    ) -> None:
        """Convert matplotlib figure to LaTeX code and save to destination.

        Parameters
        ----------
        fig : matplotlib.figure.Figure
            The matplotlib figure to convert
        destination : str
            Path where to save the LaTeX code
        standalone : bool, default=False
            If True, creates a standalone LaTeX document that can be compiled directly
        extra_axis_parameters : set, optional
            Additional TikZ axis parameters to include

        Raises
        ------
        ImportError
            If tikzplotlib is not installed

        Returns
        -------
        None

        """
        if self._tikzplotlib is None:
            raise ImportError(
                "tikzplotlib is required for LaTeX output. "
                "Install it with 'pip install tikzplotlib'"
            )
        # Ensure destination directory exists
        os.makedirs(
            os.path.dirname(destination) if os.path.dirname(destination) else ".",
            exist_ok=True,
        )

        # Set default extra parameters if none provided
        if extra_axis_parameters is None:
            extra_axis_parameters = set()

        try:
            # Convert matplotlib figure to TikZ code
            tikz_code = self._tikzplotlib.get_tikz_code(
                fig, extra_axis_parameters=extra_axis_parameters, standalone=standalone
            )

            # Write to destination file
            with open(destination, "w", encoding="utf-8") as f:
                f.write(tikz_code)

        except Exception as e:
            raise RuntimeError(f"Failed to convert matplotlib figure to LaTeX: {e}")
