import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pickle

# URL of the data
url = "https://raw.githubusercontent.com/phyokyi/datatalk_midterm_project_202311/main/data.tsv"

# Use pandas to read the data from tab separated file
data = pd.read_csv(url, sep='\t')

# Data Preparation
data.columns = data.columns.str.lower().str.replace(' ', '_')
data.fillna(0, inplace=True)

# Encoding
data_encoded = pd.get_dummies(data)
data_encoded.columns = data_encoded.columns.str.lower().str.replace(' ', '_')

# Select the most related columns with complain column
selected_columns = ['kidhome', 'education_phd', 'education_2n_cycle', 'education_graduation', 'mntwines', 'mntgoldprods', 'year_birth', 'income','complain']
data_selected = data_encoded[selected_columns]

# Split the data into features and target variable
X = data_selected.drop('complain', axis=1)
y = data_selected['complain']

# Perform feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy}")

# Save the model
with open('complain_forecast.pkl', 'wb') as file:
    pickle.dump(model, file)