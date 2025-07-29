import pandas as pd

# Assuming df is already loaded with your CSV data

# ---- Risk Score Components ---- #

# 1. Age and Sex
df["age_score"] = ((df["sex"] == 1) & (df["age"] >= 55)) | ((df["sex"] == 0) & (df["age"] >= 65))
df["age_score"] = df["age_score"].astype(int) * 2

# 2. Smoking Score
def smoking_score(cigs_per_day):
    if cigs_per_day == 0:
        return 0
    elif cigs_per_day <= 5:
        return 2
    elif cigs_per_day <= 10:
        return 4
    elif cigs_per_day <= 15:
        return 6
    elif cigs_per_day <= 20:
        return 7
    else:
        return 11

df["smoking_score"] = df["cigarettes_per_day"].apply(smoking_score)

# 3. Secondhand Smoke Exposure
df["secondhand_score"] = df["secondhand_hours_per_week"].apply(lambda x: 2 if x >= 1 else 0)

# 4. Diabetes
df["diabetes_score"] = df["diabetes"].apply(lambda x: 6 if x == 1 else 0)

# 5. High Blood Pressure
df["bp_score"] = df["high_blood_pressure"].apply(lambda x: 5 if x == 1 else 0)

# 6. Family History of Heart Disease
df["family_history_score"] = df["family_history"].apply(lambda x: 4 if x == 1 else 0)

# 7. Waist-Hip Ratio (WHR)
def whr_score(whr):
    if whr < 0.873:
        return 0
    elif whr < 0.964:
        return 2
    else:
        return 4

df["whr_score"] = df["waist_hip_ratio"].apply(whr_score)

# 8. Psychosocial Factors (Stress & Depression)
df["psychosocial_score"] = (
    df["stress_level"].apply(lambda x: 3 if x == 1 else 0) +
    df["depression"].apply(lambda x: 3 if x == 1 else 0)
)

# 9. Dietary Factors
df["diet_score"] = (
    df["salty_food"] * 1 +
    df["fried_food"] * 1 +
    (1 - df["fruit_daily"]) * 1 +
    (1 - df["veg_daily"]) * 1 +
    df["meat_daily"] * 2
)

# 10. Physical Activity
df["activity_score"] = df["physical_activity"].apply(lambda x: 2 if x == 1 else 0)

# ---- Total INTERHEART Risk Score ---- #
score_columns = [
    "age_score", "smoking_score", "secondhand_score", "diabetes_score", "bp_score",
    "family_history_score", "whr_score", "psychosocial_score", "diet_score", "activity_score"
]
df["interheart_risk_score"] = df[score_columns].sum(axis=1)

# Save the results
df.to_csv("INTERHEART_Risk_Score_Result.csv", index=False)
print("✅ Risk Scores calculated and saved to INTERHEART_Risk_Score_Result.csv")
