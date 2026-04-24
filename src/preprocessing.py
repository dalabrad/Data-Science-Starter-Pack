import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpieza básica estándar"""
    df = df.copy()
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def convert_datetime(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Convierte columna a datetime"""
    df[col] = pd.to_datetime(df[col])
    return df
