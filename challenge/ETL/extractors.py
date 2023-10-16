# aqui se hace la extracción de los datos, cualquier fuente de datos
import pandas as pd
import requests
from datetime import datetime
from constants import BASE_FILE_DIR, ROOT_DIR
import os
import logging

log = logging.getLogger()


class Extractor:
    # place holders
    file_path_crib = "{category}/{year}-{month:02d}/{category}-{day:02d}-{month:02d}-{year}.csv"
    
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def extract(self, date_str:str=None): # why the date_srt??
        """
            Args:
                date_str: string in the format "YYYY-MM-DD"

        """
        r = requests.get(self.url)
        r.encoding = 'utf-8'
        date = datetime.now()
        if date_str is not None:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        category = self.name

        # create files and fill the place holders
        file_path = BASE_FILE_DIR.joinpath(self.file_path_crib.format(category=category, 
                                                                 year=date.year, 
                                                                 month=date.month, 
                                                                 day=date.day)
                                                                 )
        
        # create the file
        file_path.parent.mkdir(parents=True, exist_ok=True)
        log.info(f"Creating file: {file_path}")

        # write the file
        with open(file=file_path, mode='w') as f:
            f.write(r.text)

        return file_path
    
    def columns_rename(self, df:pd.DataFrame, old_colums: list, new_columns: list) -> pd.DataFrame:
        """
            Exchange the old columns names for the new columns names
        """
        list_changes = {old:new for old, new in zip(old_colums, new_columns) if old in df.columns}
        print(list_changes)

        try:
            df = df.rename(columns=list_changes) 
            return df 
        except Exception:
            print("The columns names not exist")

    def transforms(self, df=pd.DataFrame()) -> pd.DataFrame:
        """
            Args:
                df: pandas dataframe
        
            Returns:
                df: pandas dataframe
        """
        norm_columns = [
            "cod_localidad",
            "id_provincia",
            "id_departamento",
            "categoría",
            "provincia",
            "localidad",
            "nombre",
            "domicilio",
            "código postal",
            "código postal",
            "número de teléfono",
            "mail",
            "web"
        ]

        old_columns = [
            'Cod_Loc', 
            'IdProvincia',
            'IdDepartamento',
            'categoria',
            'provincia',
            'localidad',
            'nombre',
            'direccion',
            'CP', 
            'cp', 
            'telefono',
            'Mail', 
            'Web',
        ]

        df: pd.DataFrame = self.columns_rename(df, old_columns, norm_columns)
        #columns = [i in norm_columns for i in df.columns]
        
        return df#[columns]