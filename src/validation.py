"""Input data quality validation."""

import pandas as pd
from src.config import REQUIRED_COLUMNS, SCORE_MIN, SCORE_MAX, VALID_CODE_PREFIX


def validate_schema(df: pd.DataFrame) -> bool:
    """Checks if all required columns are present."""
    pass


def validate_pseudonymization(df: pd.DataFrame) -> bool:
    """Checks that child_id starts with SP prefix."""
    pass


def validate_score_range(df: pd.DataFrame) -> bool:
    """Checks that scores are within valid range."""
    pass


def validate_all(df: pd.DataFrame) -> bool:
    """Runs all validation checks."""
    pass
