# en este archivo debe ejecutarse el ETL o pipeline
from ETL.extractors import Extractor
from datetime import datetime
import pandas as pd
from cfg import museo_ds, cines_ds, espacios_ds
from constants import BASE_FILE_DIR
import logging
from ETL.loaders import CinesInsightsLoader, SizeByCategoryLoader, SizeBySourceLoader, SizeByCatProvLoader

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

extractor_dicts={
    "museo": Extractor(museo_ds["name"], museo_ds["url"]),
    "cines": Extractor(cines_ds["name"], cines_ds["url"]),
    "espacios": Extractor(espacios_ds["name"], espacios_ds["url"]),
}

def extract_raw(date_str:str=None) -> dict:
    log.info("Extracting raw data")
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    file_paths = {}
    for name, extractor in extractor_dicts.items():
        file_paths[name] = extractor.extract(date_str=date_str)
    log.info(f"Raw data extracted... in {file_paths}")
    return file_paths

def merge_raw(file_paths:dict, out_path_csv=str) -> pd.DataFrame:
    # tengo tres data frames y quiero hacer un merge de los tres
    """
        
    """
    dfs_transformed = []
    log.info("Merge dfs")
    for name, extractor in extractor_dicts.items():
        df = pd.read_csv(file_paths[name], encoding="latin-1")
        dft = extractor.transforms(df)
        dfs_transformed.append(dft)
    pd.concat(dfs_transformed, axis=0).to_csv(path_or_buf=out_path_csv, index=False, encoding="latin-1")
    log.info(f"Merged dfs in {out_path_csv}")
    
    return out_path_csv

def run_pipeline(date:str=None):

    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    #extract
    file_paths = extract_raw(date_str=date)
    #transform
    merge_path = BASE_FILE_DIR / f"merge_df_{date}.csv"
    merge_raw(file_paths=file_paths, out_path_csv=merge_path)
    #load
    CinesInsightsLoader().load_table(merge_path)
    SizeByCategoryLoader().load_table(merge_path)
    SizeBySourceLoader().load_table(merge_path)
    SizeByCatProvLoader().load_table(merge_path)
    log.info(f"Done")
    pass

if __name__ == "__main__":
    run_pipeline()
    pass