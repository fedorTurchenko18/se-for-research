"""Tests for output plots formatters."""

import pandas as pd
import matplotlib.pyplot as plt
from src.io_formatters.output import LatexWriter, ImageWriter

def test_writers(tmp_path):
    """Load conversion matrix and test saving plots as PNG and LaTeX files."""
    cm = pd.read_csv('tests/data/cm.csv').values

    """Test saving a plot as a PNG image."""
    fig, ax = plt.subplots()
    ax.imshow(cm, cmap='viridis')

    image_writer = ImageWriter()
    destination = tmp_path / "test_plot.png"
    image_writer.save_output(fig, str(destination))

    assert destination.exists(), "PNG file was not created"
    plt.close(fig)

    """Test saving a plot as LaTeX code."""
    fig, ax = plt.subplots()
    ax.imshow(cm, cmap='viridis')

    latex_writer = LatexWriter()
    destination = tmp_path / "test_plot.tex"
    latex_writer.save_output(fig, str(destination))

    assert destination.exists(), "LaTeX file was not created"
    plt.close(fig)


if __name__ == "__main__":
    test_writers(tmp_path=".")
