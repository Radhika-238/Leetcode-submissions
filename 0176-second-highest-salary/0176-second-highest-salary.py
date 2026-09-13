import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    max_sal = employee['salary'].max()
    second_max = employee[employee['salary'] < max_sal]['salary'].max()
    return pd.DataFrame({'SecondHighestSalary' : [second_max] })