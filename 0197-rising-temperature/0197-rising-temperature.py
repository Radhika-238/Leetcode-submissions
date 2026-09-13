import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate')
    df = weather[
        ((weather['recordDate'] - weather['recordDate'].shift(1)).dt.days == 1)
        &
        (weather['temperature'] > weather['temperature'].shift(1))
    ]

    return df[['id']]

