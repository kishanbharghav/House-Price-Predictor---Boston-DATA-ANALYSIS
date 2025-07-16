import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os

# Load CSV with safe path for Streamlit Cloud or local
dir_path = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(dir_path, "train.csv")
df = pd.read_csv(csv_path)

# Use only numeric columns and drop any with NA
df = df.select_dtypes(include=[np.number]).dropna(axis=1)

# All numeric features except target
full_features = df.drop(['Id', 'SalePrice'], axis=1).columns.tolist()
basic_features = ["MSSubClass", "LotArea", "OverallQual", "OverallCond", "YearBuilt"]

# Streamlit UI
st.title("🏡 House Price Prediction")
st.write("Predict house prices using basic or advanced options.")

# Toggle for advanced input
advanced_mode = st.checkbox("Enable Advanced Mode (33 features)")
features_to_use = full_features if advanced_mode else basic_features

# Train model
X = df[features_to_use]
y = df["SalePrice"]
model = LinearRegression()
model.fit(X, y)

# Collect input
st.subheader("Enter Feature Values")
user_input = {}
for col in features_to_use:
    default_val = float(df[col].mean())
    val = st.number_input(col, value=default_val, key=col)
    user_input[col] = val

# Prediction
if st.button("Predict"):
    input_df = pd.DataFrame([user_input])
    pred = model.predict(input_df)[0]
    inr_price = pred * 83  # Approx. USD to INR

    st.success(f"💰 Predicted House Price: ${pred:,.2f} (₹{inr_price:,.2f})")
