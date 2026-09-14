import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:

    activity['first_login'] = activity.groupby('player_id')['event_date'].transform('min')
    print ( activity)

    activity = activity.drop_duplicates('player_id')
    return  activity[['player_id', 'first_login']]
