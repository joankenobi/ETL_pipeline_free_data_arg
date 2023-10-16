# aqui se hace la carga de los datos a la base de datos????
from sqlalchemy import create_engine
from cfg import DB_CONSTR
import constants
import pandas as pd
import logging

log=logging.getLogger()

engine=create_engine(DB_CONSTR)

class BaseLoader:

    def load_table(self, df:pd.DataFrame):
        try:
            df.to_sql(self.table_name, con=engine, if_exists="replace", index=False)
        except Exception as e:
            log.error(f"Error loading table {self.table_name} error: {e}")

class CinesInsightsLoader(BaseLoader):
    table_name = constants.CINE_INSIGHTS_TABLE_NAME

    def load_table(self, file_path:str):
        df = pd.read_csv(file_path, encoding="latin-1")
        count_si= lambda x: sum(x=="Si")
        insight_df = df.groupby("provincia", as_index=False).agg(
            cines = pd.NamedAgg(column="provincia", aggfunc="count"),
            pantallas = pd.NamedAgg(column="pantallas", aggfunc="sum"),
            butacas = pd.NamedAgg(column="butacas", aggfunc="sum"),
            espacio_incaa = pd.NamedAgg(column="espacio_incaa", aggfunc=count_si),
            )
        return super().load_table(insight_df)

class SizeByCategoryLoader(BaseLoader):
    table_name = constants.CATEGORY_COUNT_TABLE_NAME

    def load_table(self, file_path:str):
        df = pd.read_csv(file_path, 
                        encoding="latin-1")
        
        serie_category = df.value_counts("categoría")

        return super().load_table(serie_category.reset_index())
    
class SizeBySourceLoader(BaseLoader):
    table_name = constants.SOURCE_SIZE_TABLE_NAME

    def load_table(self, file_path:str):
        df = pd.read_csv(file_path, 
                        encoding="latin-1")
        serie_source = df.value_counts("fuente")

        return super().load_table(serie_source.reset_index())
    
class SizeByCatProvLoader(BaseLoader):
    table_name = constants.PROV_CAT_COUNT_TABLE_NAME

    def load_table(self, file_path:str):
        df = pd.read_csv(file_path, 
                        encoding="latin-1")
        serie_cat_prov = df.groupby(["provincia","categoría"]).agg(
        count=("categoría","count") #*new_name_column = ("column_df map", "agg funtion")*
        )
        return super().load_table(serie_cat_prov.reset_index())