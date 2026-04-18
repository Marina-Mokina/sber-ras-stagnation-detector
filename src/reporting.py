"""Report export: CSV, plots, text summary."""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from src.config import COL_CHILD, COL_DOMAIN, COL_DATE, COL_SCORE, LEVEL


def export_csv(stagnation_df: pd.DataFrame, output_path: Path):
    """Exports stagnation report to CSV file."""
    csv_path = output_path / 'stagnation_report.csv'
    stagnation_df.to_csv(csv_path, index=False)
    print(f"CSV-отчет со списком застоев сохранен: {csv_path}")


def generate_plots(original_df: pd.DataFrame, stagnation_df: pd.DataFrame, output_path: Path):
    """Generates progress plots for each detected stagnation case."""
    plots_dir = output_path / 'plots'
    plots_dir.mkdir(parents=True, exist_ok=True)

    for _, row in stagnation_df.iterrows():
        child = row[COL_CHILD]
        domain = row[COL_DOMAIN]

        subset = original_df[(original_df[COL_CHILD] == child) &
                             (original_df[COL_DOMAIN] == domain)].sort_values(COL_DATE)

        if len(subset) < 2:
            continue

        plt.figure(figsize=(10, 6))
        plt.plot(subset[COL_DATE], subset[COL_SCORE], marker='o', linewidth=2, label='Баллы')
        plt.title(f'{child} - {domain}', fontsize=14)
        plt.xlabel('Дата')
        plt.ylabel('Баллы')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()

        plt.savefig(plots_dir / f'{child}_{domain}.png', dpi=100)
        plt.close()

    print(f"Графики сохранены:  {plots_dir}")


def generate_summary(stagnation_df: pd.DataFrame, output_path: Path):
    """Creates text summary report for supervisor."""
    summary_path = output_path / 'summary.md'

    if len(stagnation_df) == 0:
        summary = """# Отчет об отсутствии прогресса

Застой не обнаружен. Все дети показывают прогресс.
"""
    else:
        summary = f"""# Отчет об отсутствии прогресса

## Статистика
- **Найдено случаев застоя:** {len(stagnation_df)}
- **Затронуто детей:** {stagnation_df[COL_CHILD].nunique()}
- **Высокий риск:** {len(stagnation_df[stagnation_df[LEVEL] == 'high'])}
- **Средний риск:** {len(stagnation_df[stagnation_df[LEVEL] == 'medium'])}
- **Низкий риск:** {len(stagnation_df[stagnation_df[LEVEL] == 'low'])}

## Рекомендации
1. **Высокий риск** — разобрать срочно на командной встрече
2. **Средний риск** — запланировать обсуждение в ближайшую неделю
3. **Низкий риск** — продолжить наблюдение

Полный список случаев в файле `stagnation_report.csv`

Графики динамики в папке `plots/`
"""

    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"Текстовый отчет с рекомендациями создан: {summary_path}")
