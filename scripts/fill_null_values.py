import pandas as pd

def fill_null_with_mode(df):

    for column in df.select_dtypes(include=['object']).columns:
        mode_values = df[column].mode()[0]
        
        df[column].fillna(mode_values, inplace = True)

    return df

def fill_null_with_mean(df):

    df.fillna(df.mean(numeric_only =True), inplace = True)

    return df
    