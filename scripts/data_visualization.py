import matplotlib.pyplot as plt


def univariate_analysis(df, column):
    """Performs univariate analysis based on column type"""
    plt.figure(figsize=(8, 5))
    plt.title(f"Distribution of {column}")
    if df[column].dtype in ['int64', 'float64']:
        plt.hist(df[column], bins=20)
        plt.ylabel("Frequency")
        plt.xlabel(column)
    elif df[column].dtype == 'object':
        df[column].value_counts().nlargest(10).plot(kind='bar')
        plt.ylabel("Count")
        plt.xticks(rotation = 45, ha = 'right')
        plt.xlabel(column)
    else:
        print(f"Skipping column '{column}' because data type not suitable for uni-variate analysis")

    plt.tight_layout()
    plt.show()