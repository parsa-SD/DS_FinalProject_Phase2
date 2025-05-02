import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from pathlib import Path

def preprocess(df):
    # Drop rows with missing values (you can customize this)
    df = df.dropna()

    # Select only numeric columns to normalize
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

    # Initialize scaler and fit-transform the numeric data
    scaler = MinMaxScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df

data_array  = ["1min", "5min", "15min", "30min", "1H", "1D"];
        
for arr in data_array :
    if __name__ == "__main__":
        df = pd.read_csv(f"raw_data/raw_data_{arr}.csv")
        df = preprocess(df)
        
        project_root = Path(__file__).resolve().parent.parent
        data_dir = project_root / "preprocessed_data"
        data_dir.mkdir(parents=True, exist_ok=True)  # Create if doesn't exist
        output_path = data_dir / f"preprocessed_data_{arr}.csv"
        df.to_csv(output_path, index=False)


