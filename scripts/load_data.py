import pandas as pd
from database_connection import connect_db
from pathlib import Path

def load_data(interval):
    conn = connect_db()
    df = pd.read_sql_query(f"SELECT * FROM Nasdaq_{interval}", conn)
    conn.close()
    return df

data_array  = ["1min", "5min", "15min", "30min", "1H", "1D"];

for arr in data_array :
    if __name__ == "__main__":
        df = load_data(arr)
        
        # Define and create the data folder safely
        project_root = Path(__file__).resolve().parent.parent
        data_dir = project_root / "raw_data"
        data_dir.mkdir(parents=True, exist_ok=True)  # Create if doesn't exist
        output_path = data_dir / f"raw_data_{arr}.csv"
        df.to_csv(output_path, index=False)


