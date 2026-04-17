"""Report export: CSV, plots, text summary."""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from src.config import OUTPUT_DIR, PLOTS_DIR


def export_csv(stagnation_df: pd.DataFrame, output_path: Path):
    """Exports stagnation report to CSV file."""
    pass


def generate_plots(original_df: pd.DataFrame, stagnation_df: pd.DataFrame, output_path: Path):
    """Generates progress plots for each detected stagnation case."""
    pass


def generate_summary(stagnation_df: pd.DataFrame, output_path: Path):
    """Creates text summary report for supervisor."""
    pass
