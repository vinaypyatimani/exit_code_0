import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")

# replace NaN values in the "Age" column with the median of the "Age" column
df[[ "Age" ]] = df[["Age"]].replace(to_replace=np.nan, value=df[["Age"]].median())

# replace NaN values in the "Embarked" column with the mode of the "Embarked" column
df[["Embarked"]] = df[["Embarked"]].fillna(df[["Embarked"]].mode().iloc[0])

# drop the "Cabin" column from the DataFrame
df = df.drop(columns=['Cabin'])

# create a new column "FamilySize" that is the sum of the "SibSp" and "Parch" columns plus 1 (for the passenger themselves)
family_size = df['SibSp'] + df['Parch'] + 1
df['FamilySize'] = family_size

# save the cleaned DataFrame to a new CSV file
df.to_csv("titanic_clean.csv", index=False)

# group the DataFrame by the "Pclass" column and calculate the mean of the "Fare" and "Survived" columns for each group 
summary = df.groupby('Pclass')[['Fare', 'Survived']].mean().reset_index()
summary = summary.rename(columns={'Fare': 'mean_fare', 'Survived': 'survival_rate'})

# save the summary DataFrame to a new CSV file
summary.to_csv("class_summary.csv", index=False)
