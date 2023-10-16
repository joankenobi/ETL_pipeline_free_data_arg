from decouple import AutoConfig # administra los datos de configuracion y enviroments
from constants import ROOT_DIR

# put a log here ......
print(f"ROOT_DIR: {ROOT_DIR}")

config = AutoConfig(search_path=ROOT_DIR) # busca el archivo .ini en la raiz del proyecto

# from teh .ini file import the next variables

try:
    DB_CONSTR = config("DB_CONSTR")
    MUSEO_URL = config("MUSEO_URL")
    CINES_URL = config("CINES_URL")
    ESPACIOS_URL = config("ESPACIOS_URL")

except Exception as e:
    print(f"Archivo .ini correcto no encontrado en la raiz del proyecto -> {ROOT_DIR}")
    raise e 

# Dictionary for the data sources
museo_ds = {
    "name" : "museo",
    "url" : MUSEO_URL,
}
cines_ds = {
    "name" : "cines",
    "url" : CINES_URL,
}
espacios_ds = {
    "name" : "espacios",
    "url" : ESPACIOS_URL,
}


# put a log here ......
print(f"MUSEO_URL: {MUSEO_URL}")
print(f"CINES_URL: {CINES_URL}")
print(f"ESPACIOS_URL: {ESPACIOS_URL}")