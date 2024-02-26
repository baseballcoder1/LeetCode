'''
https://github.com/baseballcoder1/LeetCode

LeetCode 184: Department Highest Salary

Difficulty: Medium
'''

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    view = employee.merge(department, left_on="departmentId", right_on="id", suffixes=[None, "_"]).rename(columns={"name_": "Department", "name": "Employee", "salary": "Salary"})[["Department", "Employee", "Salary"]]
    maxsalary = view.groupby("Department").max()
    return view.merge(maxsalary, on=["Department", "Salary"], how="inner", suffixes=[None, "_y"])[["Department", "Employee", "Salary"]]
