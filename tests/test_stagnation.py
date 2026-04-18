"""Tests for stagnation detection."""

import pandas as pd
from src.stagnation import detect_stagnation
from src.config import COL_CHILD, COL_DOMAIN, COL_DATE, COL_SCORE


def test_stagnation_found():
    """Should detect stagnation (scores unchanged for 30 days)."""
    df = pd.DataFrame({
        COL_CHILD: ['СП01', 'СП01'],
        COL_DOMAIN: ['Verbal_Request', 'Verbal_Request'],
        COL_DATE: pd.to_datetime(['2026-01-01', '2026-02-01']),
        COL_SCORE: [5, 5]
    })
    result = detect_stagnation(df, min_days=28)
    assert len(result) == 1
    assert result['delta'].iloc[0] == 0


def test_no_stagnation_when_progress():
    """No stagnation if there is progress."""
    df = pd.DataFrame({
        COL_CHILD: ['СП01', 'СП01'],
        COL_DOMAIN: ['Listening', 'Listening'],
        COL_DATE: pd.to_datetime(['2026-01-01', '2026-02-01']),
        COL_SCORE: [3, 7]
    })
    result = detect_stagnation(df, min_days=28)
    assert len(result) == 0


def test_multiple_domains():
    """Different domains for the same child."""
    df = pd.DataFrame({
        COL_CHILD: ['СП01', 'СП01', 'СП01', 'СП01'],
        COL_DOMAIN: ['Social', 'Social', 'Motor_Imitation', 'Motor_Imitation'],
        COL_DATE: pd.to_datetime(['2026-01-01', '2026-02-01', '2026-01-01', '2026-02-01']),
        COL_SCORE: [5, 5, 7, 10]
    })
    result = detect_stagnation(df, min_days=28)
    assert len(result) == 1
    assert result[COL_DOMAIN].iloc[0] == 'Social'
