'''
https://github.com/baseballcoder1/LeetCode

LeetCode 185: Department Top Three Salaries

Difficulty: Hard
'''

import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    view1 = employee
    view1["rank"] = 0
    def rank(x):
        x["rank"] = x["salary"].rank(method="dense", ascending=False)
        return x
    view2 = view1.merge(department, left_on="departmentId", right_on="id", suffixes=[None, "_y"]).groupby("id_y", as_index=False).apply(rank)
    view3 = view2.query("rank <= 3").rename(columns={"name_y": "Department", "name": "Employee", "salary": "Salary"})[["Department", "Employee", "Salary"]]
    return view3
