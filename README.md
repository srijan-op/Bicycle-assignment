# 📊 Transaction prediction, risk Analysis & Visualization Project Overview

This repository contains a comprehensive data analysis project examining business metrics, customer behavior, and transaction patterns. The project includes exploratory data analysis, statistical modeling, and actionable business recommendations based on the findings.

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.8+
- `pip` or `conda` package manager

### Environment Setup

Clone this repository to your local machine:
```bash
git clone https://github.com/srijan-op/Bicycle-assignment.git
cd Bicycle-assignment
```

Create and activate a virtual environment:

Using venv:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

OR using conda:
```bash
conda create -n data-analysis python=3.8
conda activate data-analysis
```

Install required dependencies:
```bash
pip install -r requirements.txt
```

## 📁 Data Configuration
Place your data files in the `data/` directory.

Update the configuration in `config.yaml` if necessary to match your data paths.

## ▶️ Running the Analysis

This project is structured into three main levels as defined in the assignment: data acquisition, advanced analysis, and machine learning. Each part is handled in separate notebooks and scripts as follows:

---

### 🗂️ Level 1: Data Acquisition and Basic Processing

**Run this Python script to download and checkpoint raw data from GCP:**
```bash
python download_files.py
```

**Then open this notebook to explore and summarize the raw data:**
```bash
jupyter notebook summary.ipynb
```

This includes:
- File-by-file statistics (row count, nulls, distinct values, top/bottom values)
- Basic profiling for each column

---

### 🧠 Level 2: Advanced Analysis and Risk Scoring

**Open the following notebook:**
```bash
jupyter notebook advance_analysis.ipynb
```

This notebook performs:
- Advanced pattern analysis (by category, geography, time)
- Risk scoring and fraud flagging logic
- Seasonal, cohort, and anomaly detection analyses
- Business insights with visualizations

---

### 🤖 Level 3: Machine Learning Application

**Open this notebook for model training and evaluation:**
```bash
jupyter notebook models.ipynb
```

It contains:
- User-level aggregation and clustering (K-Means)
- PCA-based cluster visualization
- Linear regression for transaction value prediction
- Model performance evaluation (RMSE, MAE, R²)
- Key feature importance extraction

---

**Note:** All outputs (including visualizations and updated files) are saved under appropriate directories:
- `updated_cleaned_data/` → risk-enriched transaction files
- `visualizations_1/`, `visualizations_2/` → generated figures
- `advanced_analysis/` → outputs from cohort and seasonal analysis


## 🧠 Approach & Methodology

### 1. Business Analysis Framework

**📌 Data Exploration & Cleaning:**
- Processed large-scale transactional data (~4GB) by chunk-based loading to prevent memory overflow
- Unified data types and parsed timestamp fields for temporal analysis
- Removed or imputed missing values; flagged and removed statistical outliers

**🧠 Memory Optimization Strategy:**
- Faced MemoryError when loading full dataset; adopted `pandas.read_csv(chunksize=...)` to process data iteratively
- Used category dtype for low-cardinality columns to reduce RAM usage
- Cleared temporary variables and cached objects post-processing to manage memory efficiently

**🔧 Feature Engineering:**
- Extracted temporal features: `day_of_week`, `hour`, and `recency_seconds` from timestamps
- Calculated user-level behavioral metrics like `previous_time` and transaction frequency
- Generated risk indicators: `is_outlier`, `anomaly_flag`, and a custom `risk_score`

**📊 Pattern & Cohort Analysis:**
- Performed seasonal and cohort-style visualizations across merchants, locations, and time
- Mapped customer purchase behavior by device and geography
- Identified high-frequency and high-risk transaction clusters

**📈 Statistical Modeling:**
- Built a linear regression model using key features (recency, device, hour, etc.)
- Split dataset into train/test; applied standard scaling and one-hot encoding
- Evaluated model using RMSE (97.27), MAE (49.68), and R² (0.3595)

**🚨 Anomaly Detection & Risk Scoring:**
- Applied Isolation Forest to flag anomalous transactions
- Developed a risk scoring logic based on:
  - Anomaly presence
  - Transaction time
  - Frequency patterns
  - Amount deviation
- Added `fraud_flag` based on risk thresholds for prioritization

**💼 Business Recommendations:**
- Highlighted operational inefficiencies and risk-heavy segments (e.g., late-night online transactions)
- Recommended focus areas:
  - High-risk merchants
  - Suspicious user clusters
  - Low-frequency spikes
- Suggested next steps:
  - Integrate user profiling
  - Implement fraud alert system
  - Develop dashboard-based monitoring

### 2. Transaction Value Prediction Approach
- Linear regression model with numeric + encoded categorical features
- Feature selection based on correlation analysis
- Cross-validation to prevent overfitting
- Performance metrics focused on business application

*Note: The model achieved an R² of 0.3595, indicating moderate predictive power. This could be improved with:*
- *Additional context-rich features (user history, real-time feedback)*
- *Non-linear modeling approaches (XGBoost, Random Forest)*
- *Enhanced feature engineering for behavioral patterns*

*Note: The model achieved an R² of 0.3595, indicating moderate predictive power. This could be improved with additional context-rich features (e.g., user history, real-time feedback, external data).*

## 📁 Project Structure
```
BICYCLE-ASSIGNMENT/
│
├── advanced_analysis/             # Advanced analytical outputs
├── cleaned_data/                  # Processed data files
├── data_summary/                  # Data summary reports
├── download/                      # Downloaded raw data files
├── updated_cleaned_data/          # Updated cleaned datasets
├── visualizations_1/              # First set of visualizations
├── visualizations_2/              # Second set of visualizations
├── download_files.py              # Script to download raw dataset from gcp bucket
├── summary.ipynb                  # Basic Analysis summary of raw data
├── advance_analysis.ipynb         # Level 2 tasks : advance analysis notebook
├── models.ipynb                   # Level 3 tasks : models notebook
```

## 📊 Performance Metrics
The transaction value prediction model achieved:

- **RMSE**: 97.27
- **MAE**: 49.68
- **R²**: 0.3595

These metrics suggest moderate model performance, constrained by the nature of the dataset. Model accuracy may be enhanced through:

- Better representation of user behavior (longer history, clustering)
- Incorporation of derived or external features
- Using non-linear models (e.g., XGBoost, Random Forest)

## 📌 Final Notes
- This project balances technical depth with business interpretation.
- Future improvements could involve real-time inference, anomaly detection refinement, or integration with dashboard tools.
