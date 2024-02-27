'''
https://github.com/baseballcoder1/LeetCode

LeetCode 570: Managers with at least 5 Direct Reports

Difficulty: Medium
'''

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    view1 = employee.query("~managerId.isnull()").groupby("managerId")[["id"]].count().query("id >= 5")
    view2 = view1.merge(employee[["id", "name"]], left_on="managerId", right_on="id")[["name"]]
    return view2
