'''
https://github.com/baseballcoder1/LeetCode

LeetCode 262: Trips and Users

Difficulty: Hard
'''

import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    view1 = trips.merge(users.query("banned == 'No'"), left_on="client_id", right_on="users_id", how="inner").merge(users.query("banned == 'No'"), left_on="driver_id", right_on="users_id", how="inner").query("'2013-10-01' <= request_at <= '2013-10-03'")
    view1["canceled"] = view1.eval("status != 'completed'")
    view1["completed"] = view1.eval("status == 'completed'")
    view2 = view1[["request_at", "canceled", "completed"]].groupby("request_at", as_index=False).sum()
    view2["Cancellation Rate"] = (view2["canceled"] / (view2["completed"] + view2["canceled"])).round(2)
    view3 = view2.rename(columns={"request_at": "Day"})[["Day", "Cancellation Rate"]]
    return view3
