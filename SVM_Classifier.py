from sklearn.svm import SVC
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Pull data from Excel and select usable columns
data = pd.read_excel("C:\\Users\\Ivan Anderies\\DataScienceProjects\\LithicClassifier\\ForIvan.xlsx", sheet_name='Sheet1')
df = pd.DataFrame(data[509:])
df.drop(['Type','StratAgg','Source','Date'], axis=1)

# Extract the last character from 'PlottedFind' and create a new column
df['LastCharacter'] = df['PlottedFind'].str.extract(r'_(\d+)$')[0]

# Group by the 'LastCharacter' and calculate the mean for all columns
aggregation_functions = {col: 'mean' for col in df.columns if col != ['Type','StratAgg','Source','Date','PlottedFind','Scan','Assemblege','Treatment'] and col != 'LastCharacter'}
result = df.groupby('LastCharacter').agg(aggregation_functions).reset_index()

# Optionally, drop the 'LastCharacter' column if you don't need it in the final result
result.drop(columns=['LastCharacter'], inplace=True)

X = df
X.drop(['PlottedFind','Scan','Assemblege','Treatment'])
y = df['Assemblage']


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)















