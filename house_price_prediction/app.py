import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load and preprocess data
df = pd.read_csv("train.csv")
df = df.select_dtypes(include=[np.number]).dropna(axis=1)

# Full feature list (numeric only)
full_features = df.drop(['Id', 'SalePrice'], axis=1).columns.tolist()

# Basic 5 features for default mode
basic_features = ["MSSubClass", "LotArea", "OverallQual", "OverallCond", "YearBuilt"]

# UI Start
st.title("🏡 House Price Prediction")
st.write("Predict house prices using basic or advanced options.")

# Toggle for advanced mode
advanced_mode = st.checkbox("Enable Advanced Mode (33 features)")

# Choose feature set
features_to_use = full_features if advanced_mode else basic_features
X = df[features_to_use]
y = df["SalePrice"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Input form
st.subheader("Enter Feature Values")
user_input = {}

for col in features_to_use:
    mean_val = float(df[col].mean())
    val = st.number_input(col, value=mean_val, key=col)
    user_input[col] = val

# Prediction
if st.button("Predict"):
    input_df = pd.DataFrame([user_input])
    pred = model.predict(input_df)[0]

    # Convert USD to INR (approx conversion rate; you can update it)
    usd_to_inr = 83.0  # Use live API if you want real-time data
    inr_price = pred * usd_to_inr

    st.success(f"💰 Predicted House Price: ${pred:,.2f} (₹{inr_price:,.2f})")
