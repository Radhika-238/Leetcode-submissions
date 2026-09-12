import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    df = employee.merge(department, left_on = 'departmentId', right_on = 'id', how = 'left', suffixes = ['_emp', '_dep'])

    max_salary = df.groupby('departmentId')['salary'].transform('max')

    df = df[df['salary'] == max_salary]

    df = df.rename(columns = {'name_dep' : 'Department', 'name_emp' : 'Employee', 'salary' : 'Salary'})

    return df[['Department', 'Employee', 'Salary']]