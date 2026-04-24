import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(df, x, y, title="Time Series"):
    plt.figure(figsize=(12,5))
    plt.plot(df[x], df[y])
    plt.title(title)
    plt.show()


def plot_distribution(df, col):
    plt.figure(figsize=(8,4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()
    