# ==============================================================================
# Enhanced Exploratory Data Analysis (EDA)
# ==============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Load data
file_path = "/Users/pedrocchiedoardo/Desktop/ESAME_Satistics/Dataset_macro.xlsx"
df = pd.read_excel(file_path)

# Clean data

year_col = "year"  

# --- 3. Initial information ---
print(f"Original year range: {df[year_col].min()} → {df[year_col].max()}")
print(f"Number of initial observations: {len(df)}")

# --- 4. Null analysis before filtering  ---
nulls_before = df.isna().sum()

# --- 5. Filter (1951 ≤ year ≤ 2024) ---
# Remove all years before 1950 (too many null values) and after 2024 (because the dataset has years until 2030)
df_filtered = df[(df[year_col] > 1950) & (df[year_col] <= 2024)].reset_index(drop=True)

# --- 6. Null analysis after filtering ---
nulls_after = df_filtered.isna().sum()

# --- 7. Comparison ---
null_comparison = pd.DataFrame({
    "Nulls_before": nulls_before,
    "Nulls_after": nulls_after,
    "Difference": nulls_before - nulls_after,
    "Pct_reduction_%": ((nulls_before - nulls_after) / nulls_before.replace(0, 1) * 100).round(2)
})

print(f"\nNumber of observations after filtering: {len(df_filtered)}")
print(f"Year range after filtering: {df_filtered[year_col].min()} → {df_filtered[year_col].max()}")

print("\n📉 Reduction of null values:")
print(null_comparison.head(15))

sns.set_style("whitegrid")
plt.style.use("seaborn-v0_8-deep")

df = df_filtered

# ==============================================================================
# 1. Initial Data Overview
# ==============================================================================
print("--- Initial Data Overview ---")
print("Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)
print("\nDescriptive Statistics:")
print(df.describe())
print("\nFirst Rows:")
print(df.head())

# Optional: show categorical variable counts (if any)
cat_cols = df.select_dtypes(include="object").columns
if len(cat_cols) > 0:
    for col in cat_cols:
        print(f"\nValue counts for {col}:")
        print(df[col].value_counts().head())

# ==============================================================================
# 2. Missing Values + Visualization
# ==============================================================================
print("\n--- Missing Value Analysis ---")
missing_values = df.isnull().sum().sort_values(ascending=False)
missing_percentage = (df.isnull().sum() / len(df) * 100).sort_values(ascending=False)
missing_data = pd.concat([missing_values, missing_percentage], axis=1, keys=['Missing Count', 'Missing %'])
print(missing_data[missing_data['Missing Count'] > 0])

# Optional visualization of missing data
if 'msno' in globals():
    plt.figure(figsize=(10, 6))
    msno.matrix(df)
    plt.title("Missing Data Visualization")
    plt.show()

# ==============================================================================
# 3. Univariate Analysis
# ==============================================================================
print("\n--- Target Variable Analysis: 'BankingCrisis' ---")
crisis_counts = df['BankingCrisis'].value_counts()
crisis_percentage = df['BankingCrisis'].value_counts(normalize=True) * 100
print(crisis_counts)
print("\nCrisis Class Distribution (%):\n", crisis_percentage)

plt.figure(figsize=(8, 6))
sns.countplot(x='BankingCrisis', data=df)
plt.title('Distribution of Banking Crises')
plt.show()

# 🔸 Histograms/KDEs for numerical features
num_cols = df.select_dtypes(include=np.number).columns.drop('BankingCrisis', errors='ignore')
print("\n--- Univariate Distributions (Histograms & KDEs) ---")
df[num_cols].hist(figsize=(18, 12), bins=30)
plt.suptitle("Feature Distributions", fontsize=16)
plt.show()

# ==============================================================================
# 4. Bivariate Analysis
# ==============================================================================
print("\n--- Bivariate Analysis ---")

# 🔸 Group means: compare crisis vs. non-crisis
group_means = df.groupby('BankingCrisis')[num_cols].mean().T
print("\nMean Comparison (Crisis vs Non-Crisis):\n", group_means.head(10))

plt.figure(figsize=(10, 6))
group_means.plot(kind='bar', figsize=(12, 6), title='Average Feature Values by Crisis')
plt.tight_layout()
plt.show()

# 🔸 Pairplot (subset of variables for clarity)
sample_features = ['rGDP_pc', 'rGDP_USD', 'inv_GDP', 'finv_GDP', 'infl']
sns.pairplot(df[sample_features + ['BankingCrisis']], hue='BankingCrisis', diag_kind='kde')
plt.suptitle('Pairplot of Selected Features vs Banking Crisis', y=1.02)
plt.show()

# 🔸 Correlation heatmap
corr = df[num_cols].corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr, cmap="coolwarm", center=0)
plt.title("Correlation Heatmap")
plt.show()

# ==============================================================================
# 5. Temporal & Cross-Country Trends
# ==============================================================================
print("\n--- Temporal and Cross-Country Trends ---")

# 🔸 Global time trend for selected variables
key_vars = ['rGDP_pc', 'infl', 'inv_GDP', 'exports_GDP']
for var in key_vars:
    plt.figure(figsize=(10, 6))
    df.groupby('year')[var].mean().plot()
    plt.title(f'Global Average {var} Over Time')
    plt.xlabel('Year')
    plt.ylabel(var)
    plt.show()

# 🔸 Crisis count by year and by country
plt.figure(figsize=(10, 6))
df.groupby('year')['BankingCrisis'].sum().plot(kind='bar')
plt.title("Number of Banking Crises per Year")
plt.xlabel("Year")
plt.ylabel("Crisis Count")
plt.show()

plt.figure(figsize=(12, 6))
top_countries = df.groupby('countryname')['BankingCrisis'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette="Reds_r")
plt.title("Top 10 Countries by Total Banking Crises")
plt.xlabel("Crisis Count")
plt.ylabel("Country")
plt.show()

# ==============================================================================
# 6. Outlier Detection
# ==============================================================================
print("\n--- Outlier Detection ---")

# 🔸 IQR method
Q1 = df[num_cols].quantile(0.25)
Q3 = df[num_cols].quantile(0.75)
IQR = Q3 - Q1
outliers_iqr = ((df[num_cols] < (Q1 - 1.5 * IQR)) | (df[num_cols] > (Q3 + 1.5 * IQR))).sum()
print("Outliers detected using IQR method (per variable):\n", outliers_iqr[outliers_iqr > 0])

# 🔸 Z-score method
z_scores = np.abs((df[num_cols] - df[num_cols].mean()) / df[num_cols].std())
outliers_z = (z_scores > 3).sum()
print("\nOutliers detected using Z-score method (>|3|):\n", outliers_z[outliers_z > 0])

# Optionally visualize outliers for a key variable
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['rGDP_pc'])
plt.title("Outlier Detection - rGDP_pc")
plt.show()

# ==============================================================================
# 7. Feature Scaling Check (Optional)
# ==============================================================================
print("\n--- Feature Scaling Check ---")
scaling_stats = df[num_cols].agg(['min', 'max', 'mean', 'std']).T
print(scaling_stats.head(10))

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[num_cols])
plt.title("Feature Range Comparison (Before Scaling)")
plt.xticks(rotation=90)
plt.show()


# ==============================================================================
# 8. Feature Engineering - Lag Variables
# ==============================================================================

# Sort by country and year for proper lag calculations
df = df.sort_values(['countryname', 'year'])

# 1. Simple lags (1–3 years)
vars_lag = ['rGDP_pc', 'inv_GDP', 'finv_GDP', 'USDfx', 'CPI', 'infl', 'exports_GDP', 'imports_USD']
for var in vars_lag:
    for lag in [1, 2, 3]:
        df[f'{var}_lag{lag}'] = df.groupby('countryname')[var].shift(lag)

# 2. Growth rates / changes
for var in ['rGDP_pc', 'USDfx', 'CPI', 'exports_GDP']:
    df[f'{var}_growth'] = df.groupby('countryname')[var].pct_change()

# 3. Rolling mean & standard deviation (3 years)
for var in ['rGDP_pc', 'USDfx', 'infl']:
    df[f'{var}_mean3'] = df.groupby('countryname')[var].rolling(window=3).mean().reset_index(0, drop=True)
    df[f'{var}_vol3'] = df.groupby('countryname')[var].rolling(window=3).std().reset_index(0, drop=True)

# 4. Ratio features and their lags
df['ratio_inv_cons'] = df['inv_GDP'] / df['cons_GDP']
df['ratio_exp_imp'] = df['exports_GDP'] / df['imports_USD']
df['ratio_fx_cpi'] = df['USDfx'] / df['CPI']

for ratio in ['ratio_inv_cons', 'ratio_exp_imp', 'ratio_fx_cpi']:
    df[f'{ratio}_lag1'] = df.groupby('countryname')[ratio].shift(1)


# ==============================================================================
# 9. Final Data Cleaning - Remove Missing Values
# ==============================================================================

# Count missing values before cleaning
print("\nTotal missing values before cleaning:", df.isna().sum().sum())

# Remove rows with missing values in any column
df_clean = df.dropna().copy()

# Count how many rows remain
print(f"Total initial rows: {len(df):,}")
print(f"Remaining rows after dropna(): {len(df_clean):,}")
print(f"Rows removed: {len(df) - len(df_clean):,}")






########################### da qua in poi riguardare ###########################

########################### da qua in poi riguardare ###########################

########################### da qua in poi riguardare ###########################

########################### da qua in poi riguardare ###########################

########################### da qua in poi riguardare ###########################


########################### da qua in poi riguardare ###########################






# ==============================================================================
# Data Preparation: Train/Test Split, Scaling, and SMOTE Balancing
# ==============================================================================
# This script performs:
# 1. Stratified train/test split (maintains crisis/non-crisis proportion)
# 2. Scaling applied only on training set
# 3. SMOTE applied on training set to balance classes
# ==============================================================================

from scipy import sparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# Step 0: Dataset Definition
# -----------------------------
# df_clean = dataframe already containing lag, growth, rolling and ratio-lag features
X = df_clean.drop(columns=['BankingCrisis', 'countryname', 'year'])
y = df_clean['BankingCrisis']

# -----------------------------
# Step 1: Stratified Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    stratify=y, 
    random_state=42
)

print(f"Training set: {len(X_train):,} rows")
print(f"Test set: {len(X_test):,} rows")

# -----------------------------
# Step 2: Scaling (training only)
# -----------------------------
numerical_vars = X_train.select_dtypes(include='float64').columns.tolist()

scaler = StandardScaler()

# Fit only on training set
X_train_scaled = X_train.copy()
X_train_scaled[numerical_vars] = scaler.fit_transform(X_train[numerical_vars])

# Transform test set (using training set parameters)
X_test_scaled = X_test.copy()
X_test_scaled[numerical_vars] = scaler.transform(X_test[numerical_vars])

# -----------------------------
# Step 3: SMOTE on training set
# -----------------------------
smote = SMOTE(random_state=42)
X_train_bal, y_train_bal = smote.fit_resample(X_train_scaled, y_train)

print("\nTarget distribution after SMOTE on training set:")
print(y_train_bal.value_counts())

# Now X_train_bal, y_train_bal are balanced and ready for modeling
# X_test_scaled, y_test remain imbalanced (correct for evaluation)


# ==============================================================================
# Step 4: Exploratory Data Analysis of Datasets
# ==============================================================================

# Helper function for descriptive statistics
def dataset_summary(X, y, name="Dataset"):
    """
    Displays comprehensive summary statistics for a dataset
    
    Parameters:
    -----------
    X : DataFrame
        Feature matrix
    y : Series
        Target variable
    name : str
        Name identifier for the dataset
    """
    print(f"\n--- {name} ---")
    print(f"Rows: {len(X):,}")
    print(f"Columns: {X.shape[1]}")
    
    print("\nTarget distribution:")
    print(y.value_counts())
    
    print("\nTarget percentages:")
    print(y.value_counts(normalize=True) * 100)
    
    print("\nVariable types:")
    print(X.dtypes.value_counts())
    
    print("\nDescriptive statistics (numerical):")
    display(X.describe())
    
    print("\nVariables with null values:")
    null_counts = X.isnull().sum()
    if null_counts.sum() == 0:
        print("No missing values")
    else:
        print(null_counts[null_counts > 0])


# 1️⃣ Original training dataset
dataset_summary(X_train, y_train, "Original Training Set")

# 2️⃣ Balanced training dataset with SMOTE
dataset_summary(X_train_bal, y_train_bal, "Balanced Training Set (SMOTE)")

# 3️⃣ Test dataset
dataset_summary(X_test_scaled, y_test, "Test Set")


# ==============================================================================
# Additional Analysis: Numerical Correlations in Training Set
# ==============================================================================

plt.figure(figsize=(12, 10))
sns.heatmap(
    X_train_scaled[numerical_vars].corr(), 
    annot=True, 
    fmt=".2f", 
    cmap="coolwarm"
)
plt.title("Correlations Between Numerical Variables (Training Set)")
plt.tight_layout()
plt.show()


# ==============================================================================
# Visual Target Distribution
# ==============================================================================

plt.figure(figsize=(6, 4))
sns.countplot(x=y_train_bal)
plt.title("Target Distribution After SMOTE")
plt.xlabel("Banking Crisis")
plt.ylabel("Count")
plt.show()


# ==============================================================================
# Summary Statistics Comparison
# ==============================================================================

print("\n" + "="*80)
print("SUMMARY: Dataset Comparison")
print("="*80)

comparison_df = pd.DataFrame({
    'Dataset': ['Original Training', 'Balanced Training (SMOTE)', 'Test'],
    'Rows': [len(X_train), len(X_train_bal), len(X_test)],
    'Crisis_Count': [
        y_train.sum(), 
        y_train_bal.sum(), 
        y_test.sum()
    ],
    'Non_Crisis_Count': [
        (y_train == 0).sum(),
        (y_train_bal == 0).sum(),
        (y_test == 0).sum()
    ]
})

comparison_df['Crisis_%'] = (
    comparison_df['Crisis_Count'] / comparison_df['Rows'] * 100
).round(2)

print(comparison_df.to_string(index=False))
print("\n" + "="*80)




