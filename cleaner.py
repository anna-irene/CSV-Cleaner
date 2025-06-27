import pandas as pd

def clean_csv(df):
    # 1. Remove completely empty columns
    df = df.dropna(axis=1, how='all')

    # 2. Clean column names
    cleaned_cols = []
    for col in df.columns:
        col = col.strip().lower().replace(' ', '_')
        cleaned_cols.append(col)

    df.columns = cleaned_cols

    # 3. Convert to numeric and fill missing with median
    for col in df.columns:
        converted = pd.to_numeric(df[col], errors='coerce')
        if not converted.isnull().all():
            median = converted.median()
            df[col] = converted.fillna(median)

    # 4. Drop rows with missing text values
    for col in df.columns:
        if df[col].dtype == 'object':
            df = df.dropna(subset=[col])

    # 5. Clean string values
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip().str.lower()

    # 6. Remove outliers using IQRs method
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr
            df = df[(df[col] >= lower) & (df[col] <= upper)]

    # 7. Remove duplicate rows
    df = df.drop_duplicates()

    return df

