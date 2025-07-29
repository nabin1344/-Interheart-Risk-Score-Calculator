# -Interheart-Risk-Score-Calculator
This Python script calculates the INTERHEART Modifiable Risk Score for individuals based on cardiovascular risk factors (age, sex, smoking, diabetes, etc.) from a CSV file (heart.csv) and saves the output as HEART2.csv.
📂 Files
	•	heart.csv — Input dataset (must contain columns like age, sex, cigarettes_per_day, etc.)
	•	risk_score_calculator.py — Python script to calculate risk scores.
	•	HEART2.csv — Output file with calculated INTERHEART risk scores.
 
 📊 Input Data Requirements:
Your heart.csv file should include the following columns:
Column
age : Age of the individual
sex : 1 = Male, 0 = Female
cigarettes_per_day : Number of cigarettes smoked daily
secondhand_hours_per_week : Hours of secondhand smoke exposure weekly
diabetes : 1 = Yes, 0 = No
high_blood_pressure : 1 = Yes, 0 = No
family_history : 1 = Yes, 0 = No
waist_hip_ratio : Waist-to-hip ratio
stress_level : 1 = Several periods/ongoing, 0 = Never/some
depression: 1 = Yes, 0 = No
salty_food, fried_food, fruit_daily, veg_daily, meat_daily
Dietary factors (1 = Yes, 0 = No)
physical_activity 2 = Active, 1 = Sedentary/mild

⚙️ How to Run
	1.	Clone the repository:
git clone https://github.com/YourUsername/Interheart-Risk-Score.git
cd Interheart-Risk-Score

🖩 Risk Score Components Breakdown:
Component/Points Are below
Age & Sex : 2 points if Male ≥ 55 or Female ≥ 65
Smoking : 0-11 points based on cigarettes per day
Secondhand Smoke : 2 points if exposure ≥ 1 hour/week
Diabetes : 6 points if diabetic
High Blood Pressure : 5 points if hypertensive
Family History : 4 points if family history present
Waist-Hip Ratio: 0-4 points
Psychosocial Stress : 3 points for stress, 3 for depression
Diet: 1-2 points per unhealthy food habit
Physical Activity : 2 points if sedentary

The result will be saved in HEART_SCORE.csv, including a new column:

📢 Note:
	•	Ensure all column names in heart.csv match exactly as required.
	•	This script is based on INTERHEART Risk Score guidelines but simplified for educational purposes.

