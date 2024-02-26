'''
https://github.com/baseballcoder1/LeetCode

LeetCode 177: Nth Highest Salary

Difficulty: Medium
'''

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    column = "getNthHighestSalary(" + str(N) + ")"
    view = employee.drop_duplicates(subset="salary")
    if N <= 0 or view.shape[0] < N:
        return pd.DataFrame([None], columns=[column])
    return view.sort_values(by="salary", ascending=False).iloc[N-1:N].rename(columns={"salary": column})[[column]]
