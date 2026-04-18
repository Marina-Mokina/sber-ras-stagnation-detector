"""Logic for detecting children without progress."""

import pandas as pd
from src.config import (
    COL_CHILD, COL_DOMAIN, COL_DATE, COL_SCORE,
    MIN_DAYS_STAGNATION
)


def detect_stagnation(df: pd.DataFrame, min_days: int = MIN_DAYS_STAGNATION) -> pd.DataFrame:
    """
    Finds children without progress per domain by comparing two most recent sessions.
    """
    df_sorted = df.sort_values([COL_CHILD, COL_DOMAIN, COL_DATE])

    records = []

    for (child, domain), group in df_sorted.groupby([COL_CHILD, COL_DOMAIN]):
        if len(group) < 2:
            continue

        last_two = group.iloc[-2:]

        first_of_two = last_two.iloc[0]
        last_of_two = last_two.iloc[-1]

        days_diff = (last_of_two[COL_DATE] - first_of_two[COL_DATE]).days
        delta = last_of_two[COL_SCORE] - first_of_two[COL_SCORE]

        if days_diff >= min_days and delta <= 0:
            if delta < -5 or days_diff > 60:
                risk = 'high'
            elif delta == 0:
                risk = 'medium'
            else:
                risk = 'low'

            records.append({
                COL_CHILD: child,
                COL_DOMAIN: domain,
                'last_session_date': last_of_two[COL_DATE],
                'last_score': last_of_two[COL_SCORE],
                'previous_score': first_of_two[COL_SCORE],
                'delta': delta,
                'days_diff': days_diff,
                'risk_level': risk
            })

    return pd.DataFrame(records)
