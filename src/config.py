from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
OUTPUT_DIR = BASE_DIR / 'reports'

MIN_DAYS_STAGNATION = 28
SCORE_MIN = 0.0
SCORE_MAX = 100.0
VALID_CODE_PREFIX = 'СП'

COL_CHILD = 'child_id'
COL_DOMAIN = 'domain'
COL_DATE = 'session_date'
COL_SCORE = 'assessment_score'
LEVEL = 'risk_level'

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)