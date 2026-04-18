"""Tests for data validation."""

import pandas as pd
import numpy as np
from src.validation import validate_all
from src.config import COL_CHILD, COL_DOMAIN, COL_DATE, COL_SCORE


def test_validate_all_passes_with_correct_data():
    """Should return True when all data is valid."""
    df = pd.DataFrame({
        COL_CHILD: ['СП01', 'СП02'],
        COL_DOMAIN: ['Verbal_Request', 'Listening'],
        COL_DATE: pd.to_datetime(['2026-01-01', '2026-01-02']),
        COL_SCORE: [5, 10]
    })
    assert validate_all(df) is True


def test_validate_all_fails_on_missing_column():
    """Should return False when a required column is missing."""
    df = pd.DataFrame({COL_CHILD: ['СП01']})
    assert validate_all(df) is False


def test_validate_all_fails_on_missing_values():
    """Should return False when there are NaN values."""
    df = pd.DataFrame({
        COL_CHILD: ['СП01', np.nan],
        COL_DOMAIN: ['Verbal_Request', 'Listening'],
        COL_DATE: pd.to_datetime(['2026-01-01', '2026-01-02']),
        COL_SCORE: [5, 10]
    })
    assert validate_all(df) is False


def test_validate_all_fails_on_invalid_id():
    """Should return False when child_id does not start with СП."""
    df = pd.DataFrame({
        COL_CHILD: ['ПП01'],
        COL_DOMAIN: ['Verbal_Request'],
        COL_DATE: pd.to_datetime(['2026-01-01']),
        COL_SCORE: [5]
    })
    assert validate_all(df) is False


def test_validate_all_fails_on_score_out_of_range():
    """Should return False when score is below 0 or above 100."""
    df = pd.DataFrame({
        COL_CHILD: ['СП01'],
        COL_DOMAIN: ['Verbal_Request'],
        COL_DATE: pd.to_datetime(['2026-01-01']),
        COL_SCORE: [150]
    })
    assert validate_all(df) is False
