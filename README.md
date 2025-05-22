# 💳 Credit Card Fraud Detection using Streamlit

A sleek and interactive web app built with **Streamlit** that allows users to upload credit card transaction data and detect fraudulent activities using a pre-trained machine learning model. The model evaluates 29 numerical features (`V1` to `V28` and `Amount`) to classify each transaction as **Fraudulent** or **Normal**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" />
  <img src="https://img.shields.io/badge/Streamlit-%E2%9D%A4-red.svg" />
  <img src="https://img.shields.io/badge/Model-Joblib-green.svg" />
</p>

---

## 📽️ Demo Video

▶️ Watch how the app works in action:
A demo video has been added
---

## 🚀 Features

✅ Upload CSV files with 29 preprocessed transaction features
✅ Batch prediction using a trained ML model
✅ Visual display of predictions and fraud probability
✅ Responsive UI with hover animations and stylish interface
✅ Fraud summary (count and average probability)
✅ Fully customizable and extensible design

---

## 🧠 Model Details

The model is saved as `best_model.joblib` and is trained on preprocessed features typically derived from PCA-transformed transaction datasets (like the popular [Kaggle Credit Card Fraud Detection dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)).

**Features Required:**
`V1` to `V28`, and `Amount`

**Prediction Output:**

* `Prediction`: 1 → Fraud, 0 → Normal
* `Probability`: Probability score of being fraudulent

---

## 🛠️ Installation & Usage

### 🔧 Prerequisites

* Python 3.9+
* pip

### 📦 Clone and Set Up

```bash
git clone https://github.com/Sayeem-Velocity/Credit-Card-Fraud-Detection-Webapp.git
cd credit-card-fraud-detection-webapp
pip install -r requirements.txt
```

### 🧪 Run the App

```bash
streamlit run app.py
```

---

## 📂 Input Format

Upload a CSV file with the following **29 columns**:

```
V1, V2, V3, ..., V28, Amount
```

📌 **Note:** The model expects no missing values and all features must be numeric.

Example:

```csv
V1,V2,V3,...,V28,Amount
-1.3598,-0.0727,2.5363,...,0.2076,149.62
```

---

## 📊 Output

The app will return:

* A table of predictions and fraud probabilities
* A fraud summary including:

  * Number of fraudulent transactions detected
  * Average probability of fraud

---

## 📁 Project Structure

```
credit-card-fraud-detection-webapp/
│
├── app.py                            # 🎯 Main Streamlit application
├── best_model.joblib                 # 🧠 Pre-trained fraud detection model
├── requirements.txt                  # 📦 List of required Python packages
├── README.md                         # 📘 Project documentation
│
├── .gitignore                        # 🚫 Files/folders to ignore in Git
│
├── Codes/                            # 🛠️ Optional: Extra model training, utilities, or analysis scripts
│   └── ipynb files                   # (Example) Model training script
│
├── Dataset/                          # 📊 Raw or processed datasets (CSV format expected)
│   └── creditcard.csv                #  CSV file dataset
│
├── Video/                            # 📹 Demo video showcasing the app
│   └── Credit Card Fraud Detection.mp4           

```

---

## 🧑‍💻 Author

**S.M. Shahriar**
📧 Email: [sayeem26s@gmail.com](mailto:sayeem26s@gmail.com)
💻 GitHub: [Sayeem-Velocity](https://github.com/Sayeem-Velocity)

---

## ⭐ Show Your Support

If you found this project useful, consider giving it a ⭐ on [GitHub](https://github.com/Sayeem-Velocity/Credit-Card-Fraud-Detection-Webapp)!
