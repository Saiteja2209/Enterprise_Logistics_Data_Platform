from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Raw Folder
RAW_FOLDER = PROJECT_ROOT / "data" / "raw"


def get_csv_files():
    """
    Returns all CSV files from data/raw
    """
    return list(RAW_FOLDER.glob("*.csv"))