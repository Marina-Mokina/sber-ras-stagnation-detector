"""Input data quality validation."""

import pandas as pd
import re
from src.config import (
    COL_CHILD, COL_DOMAIN, COL_DATE, COL_SCORE,
    SCORE_MIN, SCORE_MAX, VALID_CODE_PREFIX
)


def validate_schema(df: pd.DataFrame) -> bool:
    """Checks if all required columns are present."""
    for col in [COL_CHILD, COL_DOMAIN, COL_DATE, COL_SCORE]:
        if col not in df.columns:
            print(f"Нет колонки: {col}")
            return False
    return True


def validate_no_missing(df: pd.DataFrame) -> bool:
    """Checks for missing values in required columns."""
    required_cols = [COL_CHILD, COL_DOMAIN, COL_DATE, COL_SCORE]
    for col in required_cols:
        if df[col].isna().any():
            print(f"Есть пропуски (NaN) в колонке: {col}")
            return False
    return True


def validate_id(df: pd.DataFrame) -> bool:
    """Checks that child_id starts with SP prefix."""
    for child_id in df[COL_CHILD].unique():
        if not re.match(rf'^{VALID_CODE_PREFIX}\d+$', str(child_id)):
            print(f"Неверный формат id: {child_id} (должен быть СП01, СП02...)")
            return False
    return True


def validate_score_range(df: pd.DataFrame) -> bool:
    """Checks that scores are within valid range."""
    if df[COL_SCORE].min() < SCORE_MIN or df[COL_SCORE].max() > SCORE_MAX:
        print(f"Баллы вне диапазона {SCORE_MIN}-{SCORE_MAX}")
        return False
    return True


def validate_all(df: pd.DataFrame) -> bool:
    """Runs all validation checks."""
    if not validate_schema(df):
        return False
    if not validate_no_missing(df):
        return False
    if not validate_id(df):
        return False
    if not validate_score_range(df):
        return False

    print("Все проверки пройдены")
    return True
