from pathlib import Path
import shutil

PROJECT_ROOT = Path(__file__).resolve().parents[2]

ARCHIVE_FOLDER = PROJECT_ROOT / "data" / "archive"
FAILED_FOLDER = PROJECT_ROOT / "data" / "failed"


def move_to_archive(file_path):
    ARCHIVE_FOLDER.mkdir(exist_ok=True)

    destination = ARCHIVE_FOLDER / file_path.name

    shutil.move(str(file_path), str(destination))


def move_to_failed(file_path):
    FAILED_FOLDER.mkdir(exist_ok=True)

    destination = FAILED_FOLDER / file_path.name

    shutil.move(str(file_path), str(destination))