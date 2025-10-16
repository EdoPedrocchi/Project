# Project
## Project Overview

This project aims to **predict banking crises** using a large-scale **panel dataset of macroeconomic variables** across **241 countries**, covering historical data from **1086 to 2024** and projections up to **2030**.

The target variable is **`BankingCrisis`** (binary classification), while the explanatory variables include a wide range of macroeconomic indicators.

The objective is to build interpretable and robust **machine learning models** capable of identifying early warning signals of financial crises.

## Dataset
Dataset from: [Global Macro Data](https://www.globalmacrodata.com/?utm_source=chatgpt.com)

**Variables:**
countryname, ISO3, id, year,
rGDP_pc, rGDP_USD, cons_GDP, inv_GDP, finv_GDP,
exports_GDP, USDfx, CPI, infl, pop,
BankingCrisis, cons_USD, inv_USD, finv_USD, imports_USD



- **Target variable:** `BankingCrisis`  
- **Excluded identifiers:** `countryname`, `ISO3`, `id`, `year`

**Dataset type:** Panel (cross-country and time-series)  
**Period covered:** 1086–2030  
**Countries:** 241  



---
## 📖LIterature Review

WIP

---

## EDA of the data and Pre-processing
📊 Bivariate Analysis

| Variable        | No Crisis (0) | Crisis (1) |
| --------------- | ------------- | ---------- |
| **year**        | 1988.399      | 1993.548   |
| **rGDP_pc**     | 1,148,317.00  | 992,245.57 |
| **rGDP_USD**    | 283,455.03    | 514,340.68 |
| **cons_GDP**    | 80.60         | 80.56      |
| **inv_GDP**     | 23.50         | 22.78      |
| **finv_GDP**    | 22.30         | 21.76      |
| **exports_GDP** | 32.21         | 30.92      |
| **USDfx**       | 291.12        | 256.48     |
| **CPI**         | 74.16         | 44.25      |
| **infl**        | 669,305.90    | 142.38     |


🕰️ Year Range
Original: 1086 → 2030
After Filtering: 1951 → 2024
📦 Observations
Initial Observations: 58,343
After Filtering: 17,810

📉 Reduction of Null Values

| Variable      | Nulls Before | Nulls After | Difference | % Reduction |
| ------------- | ------------ | ----------- | ---------- | ----------- |
| countryname   | 0            | 0           | 0          | 0.00%       |
| year          | 0            | 0           | 0          | 0.00%       |
| rGDP_pc       | 36,110       | 3,286       | 32,824     | 90.90%      |
| rGDP_USD      | 41,918       | 4,769       | 37,149     | 88.62%      |
| cons_GDP      | 45,574       | 5,657       | 39,917     | 87.59%      |
| inv_GDP       | 43,087       | 4,982       | 38,105     | 88.44%      |
| finv_GDP      | 44,308       | 5,275       | 39,033     | 88.09%      |
| exports_GDP   | 41,636       | 4,764       | 36,872     | 88.56%      |
| USDfx         | 35,022       | 2,708       | 32,314     | 92.27%      |
| CPI           | 38,985       | 5,429       | 33,556     | 86.07%      |
| infl          | 33,105       | 5,417       | 27,688     | 83.64%      |
| pop           | 6,405        | 258         | 6,147      | 95.97%      |
| BankingCrisis | 38,410       | 8,591       | 29,819     | 77.63%      |
| cons_USD      | 45,879       | 5,960       | 39,919     | 87.01%      |
| inv_USD       | 44,195       | 5,345       | 38,850     | 87.91%      |


🧮 Dataset Info
Shape: (17,810, 17)
Data Types:
countryname → object
year → int64
rGDP_pc, rGDP_USD, cons_GDP, inv_GDP, finv_GDP, exports_GDP,
USDfx, CPI, infl, pop, BankingCrisis, cons_USD, inv_USD,
finv_USD, imports_USD → float64


📈 Descriptive Statistics (excerpt)

| Variable    | Mean        | Std Dev     | Min    | 25%      | 50%      | 75%       | Max        |
| ----------- | ----------- | ----------- | ------ | -------- | -------- | --------- | ---------- |
| year        | 1987.38     | 21.29       | 1951   | 1969     | 1987     | 2006      | 2024       |
| rGDP_pc     | 1,063,115.0 | 4,918,016.0 | 0.00   | 10,403.0 | 37,480.0 | 264,544.0 | 91,972,600 |
| cons_GDP    | 82.45       | 22.92       | 8.83   | 70.96    | 80.02    | 91.00     | 298.38     |
| inv_GDP     | 23.64       | 11.59       | -21.55 | 16.84    | 22.65    | 28.49     | 243.18     |
| exports_GDP | 38.08       | 48.44       | 0.00   | 16.78    | 28.81    | 46.76     | 1,168.42   |


🌍 Country Sample (First Rows)

| countryname | year | pop      | BankingCrisis | cons_USD | inv_USD | finv_USD | imports_USD |
| ----------- | ---- | -------- | ------------- | -------- | ------- | -------- | ----------- |
| Aruba       | 1951 | 0.038772 | NaN           | NaN      | NaN     | NaN      | NaN         |
| Aruba       | 1952 | 0.039475 | NaN           | NaN      | NaN     | NaN      | NaN         |
| Aruba       | 1953 | 0.040680 | NaN           | NaN      | NaN     | NaN      | NaN         |
| Aruba       | 1954 | 0.042311 | NaN           | NaN      | NaN     | NaN      | NaN         |
| Aruba       | 1955 | 0.044297 | NaN           | NaN      | NaN     | NaN      | NaN         |




🔢 Country Counts (sample)

| Country    | Count |
| ---------- | ----- |
| Aruba      | 74    |
| Mongolia   | 74    |
| Mozambique | 74    |
| Mauritania | 74    |
| Montserrat | 74    |


🕳️ Missing Value Analysis

| Variable      | Missing Count | Missing % |
| ------------- | ------------- | --------- |
| BankingCrisis | 8,591         | 48.24%    |
| cons_USD      | 5,960         | 33.46%    |
| cons_GDP      | 5,657         | 31.76%    |
| finv_USD      | 5,563         | 31.24%    |
| CPI           | 5,429         | 30.48%    |
| infl          | 5,417         | 30.42%    |
| inv_USD       | 5,345         | 30.01%    |
| finv_GDP      | 5,275         | 29.62%    |
| inv_GDP       | 4,982         | 27.97%    |
| rGDP_USD      | 4,769         | 26.78%    |
| exports_GDP   | 4,764         | 26.75%    |
| imports_USD   | 4,497         | 25.25%    |
| rGDP_pc       | 3,286         | 18.45%    |
| USDfx         | 2,708         | 15.20%    |
| pop           | 258           | 1.45%     |


🎯 Target Variable Analysis — BankingCrisis

| Value           | Count | Percentage |
| --------------- | ----- | ---------- |
| 0.0 (No Crisis) | 9,031 | 97.96%     |
| 1.0 (Crisis)    | 188   | 2.04%      |

📊 Bivariate Analysis

| Variable        | No Crisis (0) | Crisis (1) |
| --------------- | ------------- | ---------- |
| **year**        | 1988.399      | 1993.548   |
| **rGDP_pc**     | 1,148,317.00  | 992,245.57 |
| **rGDP_USD**    | 283,455.03    | 514,340.68 |
| **cons_GDP**    | 80.60         | 80.56      |
| **inv_GDP**     | 23.50         | 22.78      |
| **finv_GDP**    | 22.30         | 21.76      |
| **exports_GDP** | 32.21         | 30.92      |
| **USDfx**       | 291.12        | 256.48     |
| **CPI**         | 74.16         | 44.25      |
| **infl**        | 669,305.90    | 142.38     |



