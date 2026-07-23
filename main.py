from loaders.uploader import upload_files
from loaders.loader import load_tables
from validators.validator import validate
from logger.logger import logger

def main():
    logger.info("========== ETL Pipeline Started ==========")

    # Step 1: Upload CSV files to Snowflake Stage
    upload_files()

    # Step 2: Load data from Stage into RAW tables
    load_tables()

    # Step 3: Validate row counts
    validate()

    logger.info("========== ETL Pipeline Completed ==========")


if __name__ == "__main__":
    main()