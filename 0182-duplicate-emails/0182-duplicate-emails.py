import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    email_dup= person[person.duplicated('email', keep = False)]
    email_dup = email_dup[['email']].drop_duplicates()
    email_dup = email_dup.rename(columns={'email' : 'Email'})
    return email_dup