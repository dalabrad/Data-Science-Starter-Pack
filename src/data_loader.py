import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """Carga un CSV de forma estándar"""
    return pd.read_csv(path)
