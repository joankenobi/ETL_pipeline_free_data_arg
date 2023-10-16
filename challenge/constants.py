from pathlib import Path

ROOT_DIR=  Path(__file__).parent.resolve() # if fails, try Path(__file__).parent.resolve()
BASE_FILE_DIR = ROOT_DIR.joinpath("./tmp").resolve()
SQL_DIR = ROOT_DIR.joinpath("./sql").resolve()

RAW_TABLE_NAME = "raw"
CINE_INSIGHTS_TABLE_NAME = "cine_insights"
SOURCE_SIZE_TABLE_NAME = "size_by_datasource"
CATEGORY_COUNT_TABLE_NAME = "size_by_category"
PROV_CAT_COUNT_TABLE_NAME = "size_by_province"

TABLE_NAMES = [
    RAW_TABLE_NAME,
    CINE_INSIGHTS_TABLE_NAME,
    SOURCE_SIZE_TABLE_NAME,
    CATEGORY_COUNT_TABLE_NAME,
    PROV_CAT_COUNT_TABLE_NAME,
]

# put a log here ......
print(f"ROOT_DIR: -------> {ROOT_DIR} <-------")
print(f"SQL_DIR: {SQL_DIR}")
print(f"BASE_FILE_DIR: {BASE_FILE_DIR}")

