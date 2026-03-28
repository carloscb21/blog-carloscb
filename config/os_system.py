import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables de entorno desde .env si existe
load_dotenv(os.path.join(BASE_DIR, '.env'))

def get_env_var(var_name, default=None):
    """
    Obtiene una variable de entorno.
    Si no existe y no hay default, lanza ValueError.
    """
    value = os.getenv(var_name, default)
    if value is None:
        raise ValueError(f"La variable de entorno {var_name} no está definida ni exportada.")
    return value
