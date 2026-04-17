"""Logic for detecting children without progress."""

import pandas as pd
from src.config import MIN_DAYS_STAGNATION


def detect_stagnation(df: pd.DataFrame, min_days: int = 28) -> pd.DataFrame:
    """
    Finds children without progress per domain.
    """
    pass
