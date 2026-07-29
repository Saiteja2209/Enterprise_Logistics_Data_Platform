import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'python'))

from utils.file_discovery import get_csv_files
from loaders.uploader import upload_file
from loaders.loader import load_table
from validators.validator import validate_table
from utils.file_manager import move_to_archive, move_to_failed
from logger.logger import logger
from merge.merge_tables import merge_table
from schema.schema_generator import create_table_if_not_exists
from schema.schema_evolution import evolve_schema
from metadata.pipeline_audit import start_pipeline, finish_pipeline
from metadata.load_history import (
    is_file_loaded,
    log_success,
    log_failure,
)


def main():
    logger.info("=" * 60)
    logger.info("Enterprise ETL Pipeline Started")
    logger.info("=" * 60)

    files = get_csv_files()

    logger.info(f"Found {len(files)} CSV files")

    run_id = start_pipeline("Enterprise Logistics ETL")

    processed = 0
    failed = 0

    for file in files:
        if is_file_loaded(file):

            logger.info(f"{file.name} already loaded. Skipping.")

            continue

        logger.info("-" * 60)
        logger.info(f"Processing {file.name}")

        try:
            create_table_if_not_exists(file)

            evolve_schema(file)

            upload_file(file)

            load_table(file)

            validate_table(file)

            merge_table(file)
            move_to_archive(file)

            table = file.stem.upper()
            log_success(
                file,
                table,
                0
            )
            logger.info(f"{file.name} processed successfully")
            processed += 1

        except Exception as e:
            table = file.stem.upper()
            log_failure(file, table)
            logger.error(f"{file.name} failed")
            logger.error(str(e))
            failed += 1
            if file.exists():
                move_to_failed(file)

    finish_pipeline(
        run_id,
        "SUCCESS" if failed == 0 else "FAILED",
        processed,
        failed
    )

    logger.info("=" * 60)
    logger.info("Pipeline Completed Successfully")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
