# Day 5: Pandas and Data Analysis

This repository contains Python exercises focusing on the Pandas library. We process and analyze the famous Titanic dataset.

---

## Exercise 1 — `analysis.py` (Titanic Dataset Analysis)
- Loads the `titanic.csv` dataset using Pandas.
- Answers 10 specific statistical and data manipulation questions using pure Python and Pandas (no Jupyter Notebook).
- **Features**:
  - Computes exact passenger counts and survival percentages.
  - Groups data by Passenger Class, Gender, Embarkation Port, and custom Age Groups.
  - Imputes missing Age values dynamically using the median age for the respective passenger class.
  - Cleans data by dropping rows with missing Cabin entries.
  - Locates and extracts specific individual records (e.g., the oldest surviving passenger).
- **Usage**:
  ```bash
  python3 analysis.py
  ```

---

## Output Snapshot
Running the script yields clear, terminal-friendly output for all 10 questions:
```text
Titanic Dataset Analysis
==============================

01. Survival Counts and Percentages:
Counts:
Survived
0    549
1    342
Percentages (%):
Survived
0    61.62
1    38.38

02. Survival Rate by Passenger Class (%):
Pclass
1    62.96
2    47.28
3    24.24

03. Average Age of Survivors vs Non-Survivors:
Survived
0    30.63
1    28.34

04. Embarkation port with the highest survival rate: C (55.36%)

05. Passengers with missing age values: 177
    Missing ages filled with the median age for that passenger class.

06. Oldest Surviving Passenger:
    Name:  Barkworth, Mr. Algernon Henry Wilson
    Age:   80.0
    Class: 1

07. Survival Rate by Gender (%):
Sex
female    74.20
male      18.89

08. Survival Rate per AgeGroup (%):
AgeGroup
Adult (18-60)    36.51
Child (<18)      53.98
Senior (60+)     22.73

09. Survival Rate among 3rd Class Passengers by Gender (%):
Sex
female    50.00
male      13.54

10. Missing Cabin Data Removed:
    Rows remaining: 204
    Percentage of original data kept: 22.90%
```

---

## Data Reflection

**What was the most surprising finding from the data?**
The stark contrast in survival rates between demographics was striking—especially the compounded effect of gender and class. While females overall had a 74.20% survival rate compared to males at 18.89%, the disparity extended sharply into third class, where only 13.54% of males survived compared to 50.00% of females. It clearly quantifies how strictly the "women and children first" protocol was followed and how much of an advantage being in 1st class offered (62.96% survival).

**What would you investigate next if you had more time?**
If I had more time, I would investigate the impact of family size on survival by creating a new feature combining `SibSp` (siblings/spouses) and `Parch` (parents/children) to see if large families or solo travelers fared worse. I would also explore the relationship between the `Fare` paid and survival chances, particularly mapping out exactly where the missing `Cabin` entries were located to see if proximity to the lifeboats played a major factor.

---

## Run

```bash
python3 analysis.py
```
