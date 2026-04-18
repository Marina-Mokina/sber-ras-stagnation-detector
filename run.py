"""Runs the pipeline."""

import click
import pandas as pd
from pathlib import Path
from src.validation import validate_all
from src.stagnation import detect_stagnation
from src.reporting import export_csv, generate_plots, generate_summary


@click.command()
@click.option('--input', '-i', required=True, help='Путь к Excel файлу')
@click.option('--output', '-o', default='reports', help='Папка для отчётов')
@click.option('--min-days', '-d', default=28, help='Минимальное количество дней без прогресса')
def main(input: str, output: str, min_days: int):
    """Run the stagnation detector."""
    output_path = Path(output)
    output_path.mkdir(parents=True, exist_ok=True)

    df = pd.read_excel(input)

    if not validate_all(df):
        print("Ошибка валидации. Проверьте формат данных.")
        return

    stagnation_df = detect_stagnation(df, min_days=min_days)

    export_csv(stagnation_df, output_path)
    generate_plots(df, stagnation_df, output_path)
    generate_summary(stagnation_df, output_path)


if __name__ == '__main__':
    main()
