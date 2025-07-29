
##Direct CSV file read#####

import pandas as pd

# Load your data
df = pd.read_csv("heart.csv")  # Replace with actual file path

# ---- Risk Score Components ---- #

# 1. Age and Sex (Assume columns 'age' and 'sex' where sex: 1=male, 0=female)
df["age_score"] = ((df["sex"] == 1) & (df["age"] >= 55)) | ((df["sex"] == 0) & (df["age"] >= 65))
df["age_score"] = df["age_score"].astype(int) * 2

# 2. Smoking (Assume 'cigarettes_per_day')
def smoking_score(x):
    if x == 0:
        return 0
    elif x <= 5:
        return 2
    elif x <= 10:
        return 4
    elif x <= 15:
        return 6
    elif x <= 20:
        return 7
    else:
        return 11
df["smoking_score"] = df["cigarettes_per_day"].apply(smoking_score)

# 3. Secondhand Smoke (Assume 'secondhand_hours_per_week')
df["secondhand_score"] = df["secondhand_hours_per_week"].apply(lambda x: 0 if x < 1 else 2)

# 4. Diabetes (1 = yes, 0 = no)
df["diabetes_score"] = df["diabetes"].apply(lambda x: 6 if x == 1 else 0)

# 5. High blood pressure (1 = yes, 0 = no)
df["bp_score"] = df["high_blood_pressure"].apply(lambda x: 5 if x == 1 else 0)

# 6. Family history (1 = yes, 0 = no)
df["family_history_score"] = df["family_history"].apply(lambda x: 4 if x == 1 else 0)

# 7. Waist to Hip Ratio (Assume 'waist_hip_ratio')
def whr_score(x):
    if x < 0.873:
        return 0
    elif x < 0.964:
        return 2
    else:
        return 4
df["whr_score"] = df["waist_hip_ratio"].apply(whr_score)

# 8. Psychosocial (Assume 'stress_level' and 'depression' as binary)
# stress_level: 0 = never/some, 1 = several periods or ongoing
# depression: 1 = yes, 0 = no
df["psychosocial_score"] = df["stress_level"].apply(lambda x: 3 if x == 1 else 0) + \
                           df["depression"].apply(lambda x: 3 if x == 1 else 0)

# 9. Dietary factors (Assume each as binary: 1=yes, 0=no)
df["diet_score"] = (
    df["salty_food"] * 1 +
    df["fried_food"] * 1 +
    (1 - df["fruit_daily"]) * 1 +
    (1 - df["veg_daily"]) * 1 +
    df["meat_daily"] * 2
)

# 10. Physical activity (Assume 'physical_activity' 2 = active, 1 = sedentary/mild)
df["activity_score"] = df["physical_activity"].apply(lambda x: 2 if x == 1 else 0)

# ---- Final Score ---- #
df["interheart_risk_score"] = df[
    ["age_score", "smoking_score", "secondhand_score", "diabetes_score", "bp_score",
     "family_history_score", "whr_score", "psychosocial_score", "diet_score", "activity_score"]
].sum(axis=1)

# Save result
df.to_csv("HEART_SCORE.csv", index=False)
print("✅ Risk scores calculated and saved to interheart_risk_scored.csv")
