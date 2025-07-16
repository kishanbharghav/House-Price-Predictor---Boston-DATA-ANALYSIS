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
<img width="1871" height="875" alt="Screenshot 2025-07-16 193331" src="https://github.com/user-attachments/assets/53610550-019e-4e5d-a2e7-12a4fff48db8" />
<img width="1866" height="885" alt="Screenshot 2025-07-16 193350" src="https://github.com/user-attachments/assets/1103045e-f1f9-4ca8-81fe-84af674b7e12" />
<img width="1876" height="879" alt="Screenshot 2025-07-16 193403" src="https://github.com/user-attachments/assets/163fe0ec-8d8c-4e50-982e-fd0eca1ce354" />
<img width="1865" height="877" alt="Screenshot 2025-07-16 193425" src="https://github.com/user-attachments/assets/f589f16e-b142-4895-bad2-f095b5213920" />
<img width="1863" height="877" alt="Screenshot 2025-07-16 193415" src="https://github.com/user-attachments/assets/ef9cb067-1298-4ec3-8902-0bc5327eca63" />

---

## 🙌 Acknowledgements

- [Kaggle Datasets](https://www.kaggle.com/)
- [Streamlit Cloud](https://streamlit.io/)
- scikit-learn, pandas, matplotlib

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
