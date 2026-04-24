def print_shape(df):
    print(f"Shape: {df.shape}")


def missing_values(df):
    return df.isnull().sum()
