"""Small data-loading and plotting helpers for the T02 Python notebooks."""

from pathlib import Path

import pandas as pd
from plotnine import (
    aes,
    annotate,
    coord_fixed,
    element_text,
    geom_text,
    geom_tile,
    ggplot,
    labs,
    scale_fill_manual,
    theme,
    theme_void,
)


TUTORIAL_DIR = Path(__file__).resolve().parent
FIXTURE_DIR = TUTORIAL_DIR.parents[1] / "data" / "fixtures" / "linear-algebra"


def load_fixture_tables() -> dict[str, pd.DataFrame]:
    """Load the four small CSV fixtures shared by every implementation."""
    return {
        "features": pd.read_csv(FIXTURE_DIR / "feature-matrix.csv"),
        "coefficients": pd.read_csv(FIXTURE_DIR / "coefficient-vector.csv"),
        "system": pd.read_csv(FIXTURE_DIR / "linear-system.csv"),
        "expected": pd.read_csv(FIXTURE_DIR / "expected-results.csv"),
    }


def matrix_multiplication_plot(features, coefficients, predictions):
    """Build a directly labeled plotnine diagram for X @ beta."""
    tiles = []

    for row in range(features.shape[0]):
        for column in range(features.shape[1]):
            tiles.append(
                {
                    "x": column,
                    "y": 3 - row,
                    "label": f"{features[row, column]:g}",
                    "component": "Feature matrix X",
                }
            )

    for row, value in enumerate(coefficients):
        tiles.append(
            {
                "x": 3,
                "y": 3 - row,
                "label": f"{value:g}",
                "component": "Coefficients beta",
            }
        )

    for row, value in enumerate(predictions):
        tiles.append(
            {
                "x": 5,
                "y": 3 - row,
                "label": f"{value:g}",
                "component": "Predictions X beta",
            }
        )

    plot_data = pd.DataFrame(tiles)

    return (
        ggplot(plot_data, aes("x", "y", fill="component", label="label"))
        + geom_tile(width=0.82, height=0.82, color="#253238", size=0.8)
        + geom_text(size=11, color="#101820")
        + annotate("text", x=0.5, y=3.75, label="X  (3 x 2)", size=12)
        + annotate("text", x=3, y=3.75, label="beta  (2 x 1)", size=12)
        + annotate("text", x=5, y=3.75, label="X beta  (3 x 1)", size=12)
        + annotate("text", x=2, y=2, label="x", size=18, fontweight="bold")
        + annotate("text", x=4, y=2, label="=", size=18, fontweight="bold")
        + scale_fill_manual(
            values={
                "Feature matrix X": "#8ECAE6",
                "Coefficients beta": "#FFB703",
                "Predictions X beta": "#90BE6D",
            }
        )
        + coord_fixed(xlim=(-0.7, 5.7), ylim=(0.4, 4.15), ratio=1)
        + labs(
            title="Matrix multiplication keeps the outer dimensions",
            subtitle="(3 x 2) x (2 x 1) -> (3 x 1): the inner dimensions match",
        )
        + theme_void()
        + theme(
            figure_size=(10, 5),
            legend_position="none",
            plot_title=element_text(size=16, weight="bold"),
            plot_subtitle=element_text(size=12),
        )
    )
