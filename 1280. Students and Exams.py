'''
https://github.com/baseballcoder1/LeetCode

LeetCode 1280: Students and Exams

Difficulty: Easy
'''

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    view1 = students.merge(examinations, on="student_id")
    view1["exam"] = 1
    view2 = view1.groupby(["student_id", "subject_name"]).count().reset_index().rename(columns={"exam": "attended_exams"})
    view3 = students.merge(subjects, how="cross")
    view4 = view3.merge(view2, on=["student_id", "subject_name"], how="left", suffixes=[None, "_y"]).sort_values(by=["student_id", "subject_name"])[["student_id", "student_name", "subject_name", "attended_exams"]].fillna({"attended_exams": 0})
    return view4
