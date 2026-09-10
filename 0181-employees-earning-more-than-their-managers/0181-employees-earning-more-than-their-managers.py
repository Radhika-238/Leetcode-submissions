import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:

    manager = employee[['id', 'salary']]

    high_salary = employee.merge(manager, left_on = 'managerId', right_on = 'id', suffixes = ('_employee', '_manager'))

    high_salary = high_salary[high_salary['salary_employee'] > high_salary['salary_manager']]

    return high_salary[['name']].rename(columns = {'name' : 'Employee'})