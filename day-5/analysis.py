import pandas as pd
import os

def main():
    # Path to the dataset
    filepath = os.path.join(os.path.dirname(__file__), 'titanic.csv')
    
    # Load dataset
    df = pd.read_csv(filepath)
    
    print("Titanic Dataset Analysis")
    print("=" * 30 + "\n")

    # 01. How many passengers survived vs. didn't? Show as counts and percentages.
    counts = df['Survived'].value_counts()
    percs = df['Survived'].value_counts(normalize=True) * 100
    print("01. Survival Counts and Percentages:")
    print("Counts:")
    print(counts.to_string())
    print("Percentages (%):")
    print(percs.round(2).to_string())
    print()

    # 02. What was the survival rate by passenger class (1st, 2nd, 3rd)?
    rate_by_class = df.groupby('Pclass')['Survived'].mean() * 100
    print("02. Survival Rate by Passenger Class (%):")
    print(rate_by_class.round(2).to_string())
    print()

    # 03. Average age of survivors vs. non-survivors.
    avg_age = df.groupby('Survived')['Age'].mean()
    print("03. Average Age of Survivors vs Non-Survivors:")
    print(avg_age.round(2).to_string())
    print()

    # 04. Which embarkation port had the highest survival rate?
    rate_by_port = df.groupby('Embarked')['Survived'].mean() * 100
    highest_port = rate_by_port.idxmax()
    print(f"04. Embarkation port with the highest survival rate: {highest_port} ({rate_by_port[highest_port]:.2f}%)")
    print()

    # 05. How many passengers have missing age values? Fill missing ages with the median age for that passenger class.
    missing_ages = df['Age'].isnull().sum()
    print(f"05. Passengers with missing age values: {missing_ages}")
    # Fill missing ages with median for their respective passenger class
    df['Age'] = df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.median()))
    print("    Missing ages filled with the median age for that passenger class.")
    print()

    # 06. Who was the oldest surviving passenger? Print their name, age, class.
    survivors = df[df['Survived'] == 1]
    oldest_idx = survivors['Age'].idxmax()
    oldest_survivor = survivors.loc[oldest_idx]
    print("06. Oldest Surviving Passenger:")
    print(f"    Name:  {oldest_survivor['Name']}")
    print(f"    Age:   {oldest_survivor['Age']}")
    print(f"    Class: {oldest_survivor['Pclass']}")
    print()

    # 07. What % of women survived vs. what % of men?
    rate_by_sex = df.groupby('Sex')['Survived'].mean() * 100
    print("07. Survival Rate by Gender (%):")
    print(rate_by_sex.round(2).to_string())
    print()

    # 08. Create a new column 'AgeGroup': Child (<18), Adult (18-60), Senior (60+). Show survival rate per group.
    def categorize_age(age):
        if pd.isna(age):
            return 'Unknown'
        elif age < 18:
            return 'Child (<18)'
        elif age <= 60:
            return 'Adult (18-60)'
        else:
            return 'Senior (60+)'
            
    df['AgeGroup'] = df['Age'].apply(categorize_age)
    rate_by_agegroup = df.groupby('AgeGroup')['Survived'].mean() * 100
    print("08. Survival Rate per AgeGroup (%):")
    print(rate_by_agegroup.round(2).to_string())
    print()

    # 09. Among 3rd class passengers, what was the survival rate for men vs. women?
    third_class = df[df['Pclass'] == 3]
    rate_3rd_sex = third_class.groupby('Sex')['Survived'].mean() * 100
    print("09. Survival Rate among 3rd Class Passengers by Gender (%):")
    print(rate_3rd_sex.round(2).to_string())
    print()

    # 10. Drop all rows with missing Cabin data. How many rows remain? What % of original data did you keep?
    original_len = len(df)
    df_clean = df.dropna(subset=['Cabin'])
    new_len = len(df_clean)
    perc_kept = (new_len / original_len) * 100
    print("10. Missing Cabin Data Removed:")
    print(f"    Rows remaining: {new_len}")
    print(f"    Percentage of original data kept: {perc_kept:.2f}%")
    print()

if __name__ == '__main__':
    main()
