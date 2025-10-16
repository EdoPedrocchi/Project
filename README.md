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
# 🧾 Data Summary Report

## 📅 Year Range
- **Original:** 1086 → 2030  
- **After Filtering:** 1951 → 2024  

## 📊 Observations
- **Initial Observations:** 58,343  
- **After Filtering:** 17,810  

---

## 📉 Reduction of Null Values

| Variable       | Nulls Before | Nulls After | Difference | % Reduction |
|----------------|--------------|--------------|-------------|--------------|
| countryname    | 0            | 0            | 0           | 0.00 |
| year           | 0            | 0            | 0           | 0.00 |
| rGDP_pc        | 36,110       | 3,286        | 32,824      | 90.90 |
| rGDP_USD       | 41,918       | 4,769        | 37,149      | 88.62 |
| cons_GDP       | 45,574       | 5,657        | 39,917      | 87.59 |
| inv_GDP        | 43,087       | 4,982        | 38,105      | 88.44 |
| finv_GDP       | 44,308       | 5,275        | 39,033      | 88.09 |
| exports_GDP    | 41,636       | 4,764        | 36,872      | 88.56 |
| USDfx          | 35,022       | 2,708        | 32,314      | 92.27 |
| CPI            | 38,985       | 5,429        | 33,556      | 86.07 |
| infl           | 33,105       | 5,417        | 27,688      | 83.64 |
| pop            | 6,405        | 258          | 6,147       | 95.97 |
| BankingCrisis  | 38,410       | 8,591        | 29,819      | 77.63 |
| cons_USD       | 45,879       | 5,960        | 39,919      | 87.01 |
| inv_USD        | 44,195       | 5,345        | 38,850      | 87.91 |

---

## 🧮 Initial Data Overview

**Shape:** `(17810, 17)`

### Data Types
```python
countryname       object
year               int64
rGDP_pc          float64
rGDP_USD         float64
cons_GDP         float64
inv_GDP          float64
finv_GDP         float64
exports_GDP      float64
USDfx            float64
CPI              float64
infl             float64
pop              float64
BankingCrisis    float64
cons_USD         float64
inv_USD          float64
finv_USD         float64
imports_USD      float64


               year       rGDP_pc      rGDP_USD      cons_GDP       inv_GDP
count  17810.000000  1.452400e+04  1.304100e+04  12153.000000  12828.000000
mean    1987.381752  1.063115e+06  2.344566e+05     82.445694     23.641202
std       21.293385  4.918016e+06  1.151318e+06     22.918222     11.591799
min     1951.000000  1.022286e-07  7.720299e-02      8.835807    -21.546017
25%     1969.000000  1.040292e+04  2.609789e+03     70.960243     16.836946
50%     1987.000000  3.748022e+04  1.236048e+04     80.024529     22.647052
75%     2006.000000  2.645438e+05  8.917573e+04     91.000511     28.490559
max     2024.000000  9.197260e+07  2.418548e+07    298.375793    243.175568

