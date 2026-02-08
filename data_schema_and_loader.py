"""
data_schema_and_loader.py

Defines the expected schema and a simple loader for CSV datasets.
"""
import pandas as pd
from typing import List, Dict

# Expected columns (example)
EXPECTED_COLUMNS = [
    "student_id",
    "age",
    "gender",  # optional
    "attendance_rate",  # 0-1
    "study_hours_per_week",
    "subject_time_json",  # JSON string or dict mapping subject->hours
    "past_scores_json",   # JSON string or dict mapping exam_date->score or subject->score
    "assignments_submitted_rate",  # 0-1
    "sleep_hours_avg",
    "engagement_score",  # 0-1 or 0-100
    "socioecon_status",   # categorical
    "label_failed"  # 0 or 1 target (exam failure)
]

def load_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Basic validation - ensure essential columns exist
    missing = [c for c in ["student_id", "attendance_rate", "study_hours_per_week", "label_failed"] if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return df
