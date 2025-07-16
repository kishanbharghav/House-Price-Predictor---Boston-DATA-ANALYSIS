# 🏡 House Price Prediction App

This is a deployed machine learning web app that predicts house prices using data from the [Kaggle House Prices Dataset](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques).  
The app is built with **Python**, **pandas**, **scikit-learn**, and **Streamlit** — and features both **Basic** and **Advanced** input modes.

---

## 🚀 Features

- ✅ Cleaned and processed the dataset with over 80 features
- 📉 Used linear regression to predict `SalePrice` of houses
- 🎛️ Toggle between:
  - **Basic Mode** – Input just 5 main features
  - **Advanced Mode** – Input all 33 numeric features
- 📊 Visualizes predictions on an interactive scatter plot
- 💰 Converts USD to INR and displays both
- 🌐 Deployed live with Streamlit Cloud

---

## 📂 Dataset

- Source: [Kaggle - House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)
- Used the `train.csv` file (cleaned and preprocessed)

---

## 💻 Tech Stack

- Python 3
- pandas, NumPy
- scikit-learn (LinearRegression)
- matplotlib (visualizations)
- Streamlit (web app framework)

---

## 🔧 Installation

1. **Clone this repo**:
    ```bash
    git clone https://github.com/your-username/house-price-predictor.git
    cd house-price-predictor
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:
    ```bash
    streamlit run app.py
    ```

---

## 🌍 Live Demo

> 🔗 [Click here to try the deployed app](https://your-app-name.streamlit.app/)

---

## 📈 Example Inputs (Basic Mode)

| Feature       | Value     |
|---------------|-----------|
| MSSubClass    | 60        |
| LotArea       | 8450      |
| OverallQual   | 7         |
| OverallCond   | 5         |
| YearBuilt     | 2003      |

---

## 📸 Screenshot

![App Screenshot](https://your-screenshot-link)

---

## 🙌 Acknowledgements

- [Kaggle Datasets](https://www.kaggle.com/)
- [Streamlit Cloud](https://streamlit.io/)
- scikit-learn, pandas, matplotlib

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
