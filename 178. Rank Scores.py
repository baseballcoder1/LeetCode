'''
https://github.com/baseballcoder1/LeetCode

LeetCode 178: Rank Scores

Difficulty: Medium
'''

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    view = scores
    view["rank"] = view["score"].rank(method="dense", ascending=False)
    return view[["score", "rank"]].sort_values(by="score", ascending=False)
