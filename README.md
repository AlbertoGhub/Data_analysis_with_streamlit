# 📊 ML Dashboard – Interactive Data Explorer with Streamlit

This project is a lightweight **Machine Learning Dashboard** built with [Streamlit](https://streamlit.io/), designed to **explore and visualise CSV datasets interactively**. Users can upload their own CSV files, preview the data, generate summary statistics, filter data, and create simple line charts — all within a clean and intuitive web interface.

---

## 🚀 Features

- Upload any `.csv` file
- Instantly preview the dataset
- View summary statistics
- Filter data based on categorical values
- Generate dynamic **line charts** from selected columns

---

## 🛠️ Tech Stack

- **Python** (pandas, matplotlib)
- **Streamlit** for web UI
- **pandas** for data manipulation
- **matplotlib** (imported but not used in current version)

---

## 📦 Installation

Make sure you have **Python 3.7+** installed. Then, follow these steps:

```bash
# Clone the repository
git clone https://github.com/your-username/ml-dashboard.git
cd ml-dashboard
```

### Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Running the App
```bash
streamlit run app.py
```

## 🧭 Step-by-Step Guide

- Upload a CSV file via the upload widget.
- The dashboard:
  - Shows the first five rows of your dataset.
  - Displays summary statistics (mean, std, min, max, etc.).
- Filter your data by selecting a column and choosing a specific value.
- Choose X and Y axes for a line chart.
- Click "Generate line chart" to visualise trends in your filtered data.

### 📸 Video of all the process (pending on doing it)


## 🔧 To-Do
- Add support for more chart types (bar, scatter, histogram)
- Custom styling and theming
- Export filtered data as CSV

# 👨‍💻 Author

Made with ❤️ by Alberto AJ - AI/ML Engineer.

📢 GitHub Badges

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/ML-ScikitLearn-orange?logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
