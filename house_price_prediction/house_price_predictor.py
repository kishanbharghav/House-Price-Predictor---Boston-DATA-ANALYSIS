import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("train.csv")
print("Data loaded. Shape:", df.shape)

# Basic Preprocessing
df = df.select_dtypes(include=[np.number]).dropna(axis=1)  # Keep only numeric columns & drop NAs
print("After dropping non-numeric and NA cols:", df.shape)

# Correlation Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), cmap='coolwarm', square=True)
plt.title("Feature Correlation")
plt.show()

# Select Features
X = df.drop(['Id', 'SalePrice'], axis=1)
y = df['SalePrice']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Predict on a single sample
sample = X_test.iloc[0:1]
sample_prediction = model.predict(sample)
print("Predicted Price for sample:", sample_prediction[0])
