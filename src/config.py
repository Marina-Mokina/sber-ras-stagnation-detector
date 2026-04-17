import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "reports"
PLOTS_DIR = OUTPUT_DIR / "plots"

MIN_DAYS_STAGNATION = 28
SCORE_MIN = 0.0
SCORE_MAX = 100.0
VALID_CODE_PREFIX = "СП"
REQUIRED_COLUMNS = ["child_code", "domain", "date", "score"]

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)