import pandas as pd
from pkg_resources import get_distribution
import pandas_ta as ta
import numpy as np
from pathlib import Path

def featuring(interval):
    data = pd.read_csv(f'.\\preprocessed_data\\preprocessed_data_{interval}.csv')
    data['Time'] = pd.to_datetime(data['Time'])
    data.set_index('Time', inplace=True)

    # Adding SMAs
    data['50_SMA'] = ta.sma(data['Close'], length=50)
    data['100_SMA'] = ta.sma(data['Close'], length=100)
    data['200_SMA'] = ta.sma(data['Close'], length=200)

    # Adding EMAs
    data['50_EMA'] = ta.ema(data['Close'], length=50)
    data['100_EMA'] = ta.ema(data['Close'], length=100)
    data['200_EMA'] = ta.ema(data['Close'], length=200)

    # Adding RSI
    data['14_RSI'] = ta.rsi(data['Close'], length=14)

    # Adding some price action indicators
    data['Change'] = data['Close'] - data['Open']
    data['5_Averagechange'] = ta.sma(data['Change'])

    # Momentum being the candles that closes outside of the previous candles range. Otherwise its being neutral.
    conds = [data['Close'] > data['High'].shift(1), data['Close'] < data['Low'].shift(1)]
    choices = ['Bullish', 'Bearish']
    data['Momentum'] = np.select(conds, choices, default='Neutral')

    # Dropping the rows with any missing values...
    data.dropna(inplace=True)

    # Adding some Time features
    season_mapping = {12: 'Winter', 1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6:'Summer', 7:'Summer', 8:'Summer', 9:'Fall', 10:'Fall', 11:'Fall'}
    data['Month_of_year'] = data.index.month
    data['Season'] = data.index.month.map(season_mapping)
    data['Day_of_week'] = data.index.day_name()

    if interval != '1D':
        data['Hour'] = data.index.hour
    else:
        data.index = data.index.date

    return data



data_array  = ["1min", "5min", "15min", "30min", "1H", "1D"];
        
for arr in data_array :
    if __name__ == "__main__":
        df = featuring(arr)
        
        project_root = Path(__file__).resolve().parent.parent
        data_dir = project_root / "featured_data"
        data_dir.mkdir(parents=True, exist_ok=True)  # Create if doesn't exist
        output_path = data_dir / f"featured_data_{arr}.csv"
        df.to_csv(output_path, index=False)



