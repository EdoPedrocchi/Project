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

| **Metric**                                 | **Value**   |
| ------------------------------------------ | ----------- |
| **Original year range**                    | 1086 → 2030 |
| **Number of initial observations**         | 58,343      |
| **Number of observations after filtering** | 17,810      |
| **Year range after filtering**             | 1951 → 2024 |

| **Variable**  | **Nulls (Before)** | **Nulls (After)** | **Difference** | **% Reduction** |
| ------------- | ------------------ | ----------------- | -------------- | --------------: |
| countryname   | 0                  | 0                 | 0              |           0.00% |
| year          | 0                  | 0                 | 0              |           0.00% |
| rGDP_pc       | 36,110             | 3,286             | 32,824         |      **90.90%** |
| rGDP_USD      | 41,918             | 4,769             | 37,149         |      **88.62%** |
| cons_GDP      | 45,574             | 5,657             | 39,917         |      **87.59%** |
| inv_GDP       | 43,087             | 4,982             | 38,105         |      **88.44%** |
| finv_GDP      | 44,308             | 5,275             | 39,033         |      **88.09%** |
| exports_GDP   | 41,636             | 4,764             | 36,872         |      **88.56%** |
| USDfx         | 35,022             | 2,708             | 32,314         |      **92.27%** |
| CPI           | 38,985             | 5,429             | 33,556         |      **86.07%** |
| infl          | 33,105             | 5,417             | 27,688         |      **83.64%** |
| pop           | 6,405              | 258               | 6,147          |      **95.97%** |
| BankingCrisis | 38,410             | 8,591             | 29,819         |      **77.63%** |
| cons_USD      | 45,879             | 5,960             | 39,919         |      **87.01%** |
| inv_USD       | 44,195             | 5,345             | 38,850         |      **87.91%** |

| **Variable**  | **Missing Count** | **Missing %** |
| ------------- | ----------------- | ------------: |
| BankingCrisis | 8,591             |    **48.24%** |
| cons_USD      | 5,960             |        33.46% |
| cons_GDP      | 5,657             |        31.76% |
| finv_USD      | 5,563             |        31.24% |
| CPI           | 5,429             |        30.48% |
| infl          | 5,417             |        30.42% |
| inv_USD       | 5,345             |        30.01% |
| finv_GDP      | 5,275             |        29.62% |
| inv_GDP       | 4,982             |        27.97% |
| rGDP_USD      | 4,769             |        26.78% |
| exports_GDP   | 4,764             |        26.75% |
| imports_USD   | 4,497             |        25.25% |
| rGDP_pc       | 3,286             |        18.45% |
| USDfx         | 2,708             |        15.20% |
| pop           | 258               |     **1.45%** |


| **Variable**  | **Type** |
| ------------- | -------- |
| countryname   | object   |
| year          | int64    |
| rGDP_pc       | float64  |
| rGDP_USD      | float64  |
| cons_GDP      | float64  |
| inv_GDP       | float64  |
| finv_GDP      | float64  |
| exports_GDP   | float64  |
| USDfx         | float64  |
| CPI           | float64  |
| infl          | float64  |
| pop           | float64  |
| BankingCrisis | float64  |
| cons_USD      | float64  |
| inv_USD       | float64  |
| finv_USD      | float64  |
| imports_USD   | float64  |

| **Variable**      | **Count** | **Mean**  | **Std**   | **Min**   | **25%** | **50% (Median)** | **75%** | **Max**    |
| ----------------- | --------- | --------- | --------- | --------- | ------- | ---------------- | ------- | ---------- |
| **year**          | 17,810    | 1987.38   | 21.29     | 1951.00   | 1969.00 | 1987.00          | 2006.00 | 2024.00    |
| **rGDP_pc**       | 14,524    | 1,063,115 | 4,918,016 | 0.0000001 | 10,403  | 37,480           | 264,544 | 91,972,600 |
| **rGDP_USD**      | 13,041    | 234,457   | 1,151,318 | 0.077     | 2,610   | 12,360           | 89,176  | 24,185,480 |
| **cons_GDP**      | 12,153    | 82.45     | 22.92     | 8.84      | 70.96   | 80.02            | 91.00   | 298.38     |
| **inv_GDP**       | 12,828    | 23.64     | 11.59     | -21.55    | 16.84   | 22.65            | 28.49   | 243.18     |
| **finv_GDP**      | 12,535    | 22.67     | 10.19     | -2.42     | 16.47   | 21.72            | 26.82   | 157.87     |
| **exports_GDP**   | 13,046    | 38.08     | 48.44     | 0.00      | 16.78   | 28.81            | 46.76   | 1,168.42   |
| **USDfx**         | 15,102    | 298.76    | 1,971.25  | 0.00      | 0.92    | 2.70             | 32.16   | 89,500     |
| **CPI**           | 12,381    | 2.36×10⁹  | 1.71×10¹¹ | 0.00      | 9.29    | 54.95            | 100.25  | 1.60×10¹³  |
| **infl**          | 12,393    | 4.56×10⁵  | 5.07×10⁷  | -72.73    | 1.95    | 4.63             | 10.36   | 5.65×10⁹   |
| **pop**           | 17,552    | 23.02     | 97.73     | 0.0006    | 0.26    | 3.32             | 11.94   | 1,451.40   |
| **BankingCrisis** | 9,219     | 0.020     | 0.141     | 0.0       | 0.0     | 0.0              | 0.0     | 1.0        |
| **cons_USD**      | 11,850    | 155,842   | 855,799   | 0.00      | 1,010   | 5,950            | 39,919  | 23,616,980 |
| **inv_USD**       | 12,465    | 49,791    | 297,127   | -3,209.72 | 225.25  | 1,596            | 11,575  | 7,786,560  |
| **finv_USD**      | 12,247    | 48,023    | 285,261   | -20.61    | 214.51  | 1,365            | 11,246  | 7,495,980  |
| **imports_USD**   | 13,313    | 46,993    | 196,206   | 0.00      | 333     | 1,934            | 13,450  | 3,966,936  |


| **Class**     | **Count** | **Percentage (%)** |
| ------------- | --------- | -----------------: |
| 0 (No Crisis) | 9,031     |         **97.96%** |
| 1 (Crisis)    | 188       |          **2.04%** |

<img width="700" height="545" alt="image" src="https://github.com/user-attachments/assets/125e1bcc-861b-4da9-8ac9-51334637ce19" />

### Univariate Analysis

<img width="1463" height="1105" alt="image" src="https://github.com/user-attachments/assets/008cccc6-4988-4161-b8dd-d7637722a1b7" />

Perfetto ✅
Ecco la **Correlation Matrix — Key Economic Variables** riformattata in **Markdown** per report o notebook, con focus sulla leggibilità.

---

## 📈 Correlation Matrix — Selected Economic Variables

| Variable        | year   | rGDP_pc | rGDP_USD | cons_GDP | inv_GDP | finv_GDP | exports_GDP | USDfx  | CPI    | infl   | pop    | cons_USD | inv_USD | finv_USD | imports_USD |
| --------------- | ------ | ------- | -------- | -------- | ------- | -------- | ----------- | ------ | ------ | ------ | ------ | -------- | ------- | -------- | ----------- |
| **year**        | 1.000  | 0.069   | 0.094    | -0.008   | 0.070   | 0.084    | 0.079       | 0.145  | 0.021  | 0.001  | 0.077  | 0.124    | 0.126   | 0.126    | 0.204       |
| **rGDP_pc**     | 0.069  | 1.000   | 0.026    | -0.066   | 0.077   | 0.067    | 0.007       | 0.553  | -0.003 | -0.002 | 0.047  | 0.015    | 0.038   | 0.032    | 0.044       |
| **rGDP_USD**    | 0.094  | 0.026   | 1.000    | -0.072   | 0.031   | 0.036    | -0.061      | 0.000  | -0.002 | -0.002 | 0.420  | 0.948    | 0.893   | 0.895    | 0.866       |
| **cons_GDP**    | -0.008 | -0.066  | -0.072   | 1.000    | -0.163  | -0.104   | -0.105      | 0.000  | 0.002  | 0.005  | -0.092 | -0.047   | -0.077  | -0.075   | -0.094      |
| **inv_GDP**     | 0.070  | 0.077   | 0.031    | -0.163   | 1.000   | 0.736    | 0.058       | 0.061  | -0.014 | -0.008 | 0.074  | 0.003    | 0.052   | 0.047    | 0.021       |
| **finv_GDP**    | 0.084  | 0.067   | 0.036    | -0.104   | 0.736   | 1.000    | 0.058       | 0.030  | -0.022 | -0.011 | 0.064  | 0.006    | 0.058   | 0.059    | 0.025       |
| **exports_GDP** | 0.079  | 0.007   | -0.061   | -0.105   | 0.058   | 0.058    | 1.000       | -0.016 | -0.013 | -0.006 | -0.094 | -0.054   | -0.045  | -0.052   | 0.004       |
| **USDfx**       | 0.145  | 0.553   | 0.000    | -0.000   | 0.061   | 0.030    | -0.016      | 1.000  | -0.002 | -0.002 | 0.035  | 0.000    | 0.018   | 0.010    | 0.021       |
| **CPI**         | 0.021  | -0.003  | -0.002   | 0.002    | -0.014  | -0.022   | -0.013      | -0.002 | 1.000  | -0.000 | -0.000 | -0.002   | -0.002  | -0.002   | -0.002      |
| **infl**        | 0.001  | -0.002  | -0.002   | 0.005    | -0.008  | -0.011   | -0.006      | -0.002 | -0.000 | 1.000  | -0.002 | -0.002   | -0.002  | -0.002   | -0.002      |
| **pop**         | 0.077  | 0.047   | 0.420    | -0.092   | 0.074   | 0.064    | -0.094      | 0.035  | -0.000 | -0.002 | 1.000  | 0.316    | 0.484   | 0.464    | 0.372       |
| **cons_USD**    | 0.124  | 0.015   | 0.948    | -0.047   | 0.003   | 0.006    | -0.054      | 0.000  | -0.002 | -0.002 | 0.316  | 1.000    | 0.892   | 0.896    | 0.911       |
| **inv_USD**     | 0.126  | 0.038   | 0.893    | -0.077   | 0.052   | 0.058    | -0.045      | 0.018  | -0.002 | -0.002 | 0.484  | 0.892    | 1.000   | 0.999    | 0.886       |
| **finv_USD**    | 0.126  | 0.032   | 0.895    | -0.075   | 0.047   | 0.059    | -0.052      | 0.010  | -0.002 | -0.002 | 0.464  | 0.896    | 0.999   | 1.000    | 0.884       |
| **imports_USD** | 0.204  | 0.044   | 0.866    | -0.094   | 0.021   | 0.025    | 0.004       | 0.021  | -0.002 | -0.002 | 0.372  | 0.911    | 0.886   | 0.884    | 1.000       |

---

### 💡 Key Insights

* Strong correlations exist among **USD-denominated variables**: `rGDP_USD`, `cons_USD`, `inv_USD`, `finv_USD`, `imports_USD` (>0.88).
* `inv_GDP` and `finv_GDP` are highly correlated (0.736), as expected for financial investment measures.
* `USDfx` shows moderate correlation with `rGDP_pc` (0.553) and `year` (0.145), indicating possible time trends or currency effects.
* Most other variables show **low correlations**, suggesting that **multicollinearity is limited** for GDP and inflation metrics.

---


### Bivariate Analysis

| **Variable**    | **Mean (No Crisis = 0)** | **Mean (Crisis = 1)** |
| --------------- | -----------------------: | --------------------: |
| **year**        |                  1988.40 |           **1993.55** |
| **rGDP_pc**     |                1,148,317 |           **992,246** |
| **rGDP_USD**    |              **283,455** |               514,341 |
| **cons_GDP**    |                **80.60** |                 80.56 |
| **inv_GDP**     |                **23.50** |                 22.78 |
| **finv_GDP**    |                **22.30** |                 21.76 |
| **exports_GDP** |                **32.21** |                 30.92 |
| **USDfx**       |               **291.12** |                256.48 |
| **CPI**         |                **74.16** |                 44.25 |
| **infl**        |            **669,305.9** |                142.38 |


<img width="1189" height="590" alt="image" src="https://github.com/user-attachments/assets/dda89ab9-eb0a-48b7-8e1d-c3437b504b5c" />

<img width="1338" height="1275" alt="image" src="https://github.com/user-attachments/assets/23cb024f-3f5c-4d4e-922a-86f0c45214aa" />


<img width="841" height="562" alt="image" src="https://github.com/user-attachments/assets/c06e2fa3-9ba9-41cc-9ab6-4ff72c53e833" />
<img width="1078" height="545" alt="image" src="https://github.com/user-attachments/assets/44c49e78-3c20-4e9d-aaed-0282547c3012" />




| **Variable**    | **Outliers (Count)** |
| --------------- | -------------------: |
| **rGDP_pc**     |                2,212 |
| **rGDP_USD**    |                2,013 |
| **cons_GDP**    |                  736 |
| **inv_GDP**     |                  424 |
| **finv_GDP**    |                  459 |
| **exports_GDP** |                  582 |
| **USDfx**       |            **2,934** |
| **CPI**         |                  386 |
| **infl**        |                1,262 |
| **pop**         |                2,388 |
| **cons_USD**    |                1,936 |
| **inv_USD**     |                2,135 |
| **finv_USD**    |                2,067 |
| **imports_USD** |                2,225 |

| **Variable**    | **Outliers (Count)** |
| --------------- | -------------------: |
| **rGDP_pc**     |                  208 |
| **rGDP_USD**    |                  133 |
| **cons_GDP**    |                  186 |
| **inv_GDP**     |                  163 |
| **finv_GDP**    |                  188 |
| **exports_GDP** |                  137 |
| **USDfx**       |                  180 |
| **CPI**         |                    4 |
| **infl**        |                    1 |
| **pop**         |                  159 |
| **cons_USD**    |                  127 |
| **inv_USD**     |                  121 |
| **finv_USD**    |                  118 |
| **imports_USD** |                  193 |



| **Variable**    |   **Min** |    **Max** |  **Mean** |   **Std** |
| --------------- | --------: | ---------: | --------: | --------: |
| **year**        |  1,951.00 |   2,024.00 |  1,987.38 |     21.29 |
| **rGDP_pc**     | 0.0000001 | 91,972,600 | 1,063,115 | 4,918,016 |
| **rGDP_USD**    |     0.077 | 24,185,480 |   234,457 | 1,151,318 |
| **cons_GDP**    |      8.84 |     298.38 |     82.45 |     22.92 |
| **inv_GDP**     |    -21.55 |     243.18 |     23.64 |     11.59 |
| **finv_GDP**    |     -2.42 |     157.87 |     22.67 |     10.19 |
| **exports_GDP** |      0.00 |   1,168.42 |     38.08 |     48.44 |
| **USDfx**       |      0.00 |     89,500 |    298.76 |  1,971.25 |
| **CPI**         |      0.00 |  1.60×10¹³ |  2.36×10⁹ | 1.71×10¹¹ |
| **infl**        |    -72.73 |   5.65×10⁹ |  4.56×10⁵ |  5.07×10⁷ |




| **Metric**                             | **Value** |
| -------------------------------------- | --------- |
| Total missing values (before cleaning) | 265,794   |
| Total initial rows                     | 17,810    |
| Remaining rows after `dropna()`        | 7,412     |
| Rows removed                           | 10,398    |


| **Metric**   | **Value**  |
| ------------ | ---------- |
| Training set | 5,929 rows |
| Test set     | 1,483 rows |


| **Class**     | **Count** | **Percentage (%)** |
| ------------- | --------: | -----------------: |
| 0 (No Crisis) |     5,788 |             97.62% |
| 1 (Crisis)    |       141 |              2.38% |


| **Class**     | **Count** |
| ------------- | --------: |
| 0 (No Crisis) |     5,788 |
| 1 (Crisis)    |     5,788 |



| **Variable**        | **Count** | **Mean**  | **Std**   | **Min**    | **25%** | **50% (Median)** | **75%** | **Max**    |
| ------------------- | --------- | --------- | --------- | ---------- | ------- | ---------------- | ------- | ---------- |
| rGDP_pc             | 5,929     | 1,251,135 | 5,412,768 | 0.0000002  | 15,065  | 44,834           | 309,058 | 91,972,600 |
| rGDP_USD            | 5,929     | 306,924   | 1,306,488 | 0.135      | 5,716   | 23,463           | 149,132 | 21,322,950 |
| cons_GDP            | 5,929     | 80.49     | 17.11     | 8.84       | 71.84   | 79.51            | 88.74   | 284.03     |
| inv_GDP             | 5,929     | 23.43     | 9.86      | -5.74      | 17.62   | 22.66            | 27.83   | 147.51     |
| finv_GDP            | 5,929     | 22.54     | 9.32      | -2.42      | 17.09   | 21.79            | 26.33   | 157.87     |
| exports_GDP         | 5,929     | 33.62     | 25.73     | 1.35       | 17.24   | 27.34            | 42.91   | 228.99     |
| USDfx               | 5,929     | 325.04    | 1,635.45  | 0.000000   | 0.987   | 5.40             | 76.71   | 33,249     |
| CPI                 | 5,929     | 60.87     | 288.45    | 0.000000   | 10.76   | 48.31            | 88.09   | 14,745     |
| infl                | 5,929     | 31.74     | 411.59    | -34.41     | 2.86    | 6.47             | 12.72   | 9,963      |
| pop                 | 5,929     | 36.66     | 127.47    | 0.04       | 2.91    | 8.26             | 24.75   | 1,380      |
| ...                 | ...       | ...       | ...       | ...        | ...     | ...              | ...     | ...        |
| USDfx_mean3         | 5,929     | 307.03    | 1,544.18  | 0.000000   | 0.97    | 5.19             | 73.36   | 31,062     |
| USDfx_vol3          | 5,929     | 29.78     | 211.04    | 0.0        | 0.01    | 0.18             | 3.70    | 6,804      |
| infl_mean3          | 5,929     | 34.26     | 296.12    | -9.43      | 2.86    | 6.47             | 12.72   | 9,963      |
| infl_vol3           | 5,929     | 29.57     | 355.22    | 0.0        | 1.04    | 2.24             | 5.40    | 13,391     |
| ratio_inv_cons      | 5,929     | 0.317     | 0.265     | -0.081     | 0.205   | 0.287            | 0.377   | 9.31       |
| ratio_exp_imp       | 5,929     | 3.72×10⁶  | 6.80×10⁷  | 3.63×10⁻⁶  | 0.0012  | 0.0063           | 0.0276  | 2.20×10⁹   |
| ratio_fx_cpi        | 5,929     | 14.93     | 95.47     | 2.15×10⁻¹² | 0.0389  | 0.262            | 3.89    | 3,483      |
| ratio_inv_cons_lag1 | 5,929     | 0.316     | 0.248     | -0.081     | 0.204   | 0.286            | 0.378   | 9.31       |
| ratio_exp_imp_lag1  | 5,929     | 3.92×10⁶  | 7.14×10⁷  | 3.78×10⁻⁶  | 0.0013  | 0.0067           | 0.0296  | 2.20×10⁹   |
| ratio_fx_cpi_lag1   | 5,929     | 16.21     | 116.38    | 2.15×10⁻¹² | 0.0413  | 0.270            | 4.07    | 5,053      |




Perfetto ✅
Ecco la sezione **Balanced Training Set (Post-SMOTE)** riformattata in **Markdown**, coerente con il resto del report.

---

## 🏋️ Balanced Training Set — SMOTE Applied

### ✅ Dataset Overview

| **Metric**     | **Value**             |
| -------------- | --------------------- |
| Rows           | 11,576                |
| Columns        | 54                    |
| Variable types | float64 (all numeric) |
| Missing values | None                  |

---

### 🎯 Target Distribution

| **Class**     | **Count** | **Percentage (%)** |
| ------------- | --------: | -----------------: |
| 0 (No Crisis) |     5,788 |              50.0% |
| 1 (Crisis)    |     5,788 |              50.0% |

> SMOTE successfully **balanced the target variable**, making it **50:50**, ideal for model training.

---


## 📊 Descriptive Statistics — Balanced Training Set (Post-SMOTE)

| **Variable**        | **Count** | **Mean** | **Std** | **Min** | **25%** | **50% (Median)** | **75%** | **Max** |
| ------------------- | --------- | -------- | ------- | ------- | ------- | ---------------- | ------- | ------- |
| rGDP_pc             | 11,576    | -0.034   | 0.789   | -0.231  | -0.227  | -0.217           | -0.168  | 16.76   |
| rGDP_USD            | 11,576    | 0.017    | 0.883   | -0.235  | -0.227  | -0.198           | -0.072  | 16.09   |
| cons_GDP            | 11,576    | -0.028   | 0.838   | -4.19   | -0.475  | -0.069           | 0.360   | 11.90   |
| inv_GDP             | 11,576    | -0.016   | 0.920   | -2.96   | -0.572  | -0.067           | 0.421   | 12.59   |
| finv_GDP            | 11,576    | -0.018   | 0.884   | -2.68   | -0.578  | -0.056           | 0.394   | 14.53   |
| exports_GDP         | 11,576    | -0.054   | 0.898   | -1.25   | -0.667  | -0.256           | 0.282   | 7.59    |
| USDfx               | 11,576    | -0.052   | 0.758   | -0.199  | -0.198  | -0.194           | -0.142  | 20.13   |
| CPI                 | 11,576    | -0.024   | 0.720   | -0.211  | -0.158  | -0.050           | 0.062   | 50.91   |
| infl                | 11,576    | 0.073    | 0.969   | -0.161  | -0.068  | -0.058           | -0.033  | 57.69   |
| pop                 | 11,576    | 0.003    | 0.889   | -0.287  | -0.252  | -0.207           | -0.038  | 10.54   |
| ...                 | ...       | ...      | ...     | ...     | ...     | ...              | ...     | ...     |
| USDfx_mean3         | 11,576    | -0.058   | 0.736   | -0.199  | -0.198  | -0.194           | -0.143  | 19.92   |
| USDfx_vol3          | 11,576    | -0.001   | 1.012   | -0.141  | -0.141  | -0.139           | -0.107  | 32.10   |
| infl_mean3          | 11,576    | 0.098    | 1.110   | -0.148  | -0.103  | -0.088           | -0.058  | 33.53   |
| infl_vol3           | 11,576    | 0.063    | 1.063   | -0.083  | -0.080  | -0.075           | -0.061  | 37.62   |
| ratio_inv_cons      | 11,576    | -0.027   | 0.787   | -1.506  | -0.416  | -0.110           | 0.250   | 33.98   |
| ratio_exp_imp       | 11,576    | -0.017   | 0.726   | -0.055  | -0.055  | -0.006           | -0.055  | 32.26   |
| ratio_fx_cpi        | 11,576    | -0.038   | 0.745   | -0.156  | -0.156  | -0.153           | -0.111  | 36.33   |
| ratio_inv_cons_lag1 | 11,576    | 0.005    | 0.799   | -1.599  | -0.414  | -0.071           | 0.278   | 36.25   |
| ratio_exp_imp_lag1  | 11,576    | -0.015   | 0.732   | -0.055  | -0.055  | -0.007           | -0.055  | 30.71   |
| ratio_fx_cpi_lag1   | 11,576    | -0.039   | 0.731   | -0.139  | -0.139  | -0.136           | -0.103  | 43.28   |



Perfetto ✅
Ecco la sezione **Test Set Overview** riformattata in **Markdown**, coerente con le altre sezioni del report.

---

## 🧪 Test Set Overview

### ✅ Dataset Information

| **Metric**     | **Value**             |
| -------------- | --------------------- |
| Rows           | 1,483                 |
| Columns        | 54                    |
| Variable types | float64 (all numeric) |
| Missing values | None                  |

---

### 🎯 Target Variable Distribution

| **Class**     | **Count** | **Percentage (%)** |
| ------------- | --------: | -----------------: |
| 0 (No Crisis) |     1,448 |             97.64% |
| 1 (Crisis)    |        35 |              2.36% |

> ⚠️ The test set remains **highly imbalanced**, reflecting the real-world distribution of banking crises.

---

### 💡 Insights

* The **test set is clean**, with **no missing values**.
* All features are **numeric (`float64`)** and ready for model evaluation.
* Target imbalance should be **kept in mind** for performance metrics:

  * Prefer **balanced metrics** (F1-score, ROC-AUC) over plain accuracy.
  * Threshold adjustment or sampling techniques are **not needed for testing**, only for training.

---

Se vuoi, posso preparare **un’unica scheda riepilogativa Markdown completa di tutto il dataset**, includendo:

* Missing values
* Train/Test split
* SMOTE / balanced training set
* Descriptive statistics (training e test)

In questo modo avresti tutto il preprocessing pronto da includere in un report unico. Vuoi che lo faccia?




Perfetto ✅
Ecco la sezione **Descriptive Statistics — Test Set (Numerical Features)** riformattata in **Markdown**, pronta per report o notebook.

---

## 📊 Descriptive Statistics — Test Set (Numerical Features)

| **Variable**        | **Count** | **Mean** | **Std** | **Min** | **25%** | **50% (Median)** | **75%** | **Max** |
| ------------------- | --------- | -------- | ------- | ------- | ------- | ---------------- | ------- | ------- |
| rGDP_pc             | 1,483     | 0.046    | 1.201   | -0.231  | -0.228  | -0.222           | -0.171  | 15.79   |
| rGDP_USD            | 1,483     | 0.021    | 0.995   | -0.235  | -0.231  | -0.217           | -0.104  | 16.46   |
| cons_GDP            | 1,483     | 0.045    | 1.073   | -3.586  | -0.472  | -0.036           | 0.527   | 11.61   |
| inv_GDP             | 1,483     | 0.010    | 0.947   | -2.346  | -0.558  | -0.092           | 0.462   | 7.76    |
| finv_GDP            | 1,483     | -0.007   | 0.976   | -2.388  | -0.587  | -0.093           | 0.405   | 9.84    |
| exports_GDP         | 1,483     | -0.065   | 0.954   | -1.240  | -0.678  | -0.297           | 0.265   | 6.97    |
| USDfx               | 1,483     | 0.026    | 1.125   | -0.199  | -0.198  | -0.195           | -0.145  | 15.66   |
| CPI                 | 1,483     | -0.027   | 0.177   | -0.211  | -0.176  | -0.051           | 0.083   | 2.49    |
| infl                | 1,483     | -0.015   | 0.784   | -0.106  | -0.071  | -0.063           | -0.047  | 28.36   |
| pop                 | 1,483     | -0.017   | 0.909   | -0.287  | -0.262  | -0.222           | -0.073  | 10.67   |
| ...                 | ...       | ...      | ...     | ...     | ...     | ...              | ...     | ...     |
| USDfx_mean3         | 1,483     | 0.020    | 1.080   | -0.199  | -0.198  | -0.195           | -0.145  | 13.38   |
| USDfx_vol3          | 1,483     | 0.032    | 1.269   | -0.141  | -0.141  | -0.140           | -0.122  | 32.48   |
| infl_mean3          | 1,483     | -0.006   | 1.056   | -0.128  | -0.106  | -0.093           | -0.072  | 29.49   |
| infl_vol3           | 1,483     | 0.002    | 1.195   | -0.083  | -0.080  | -0.077           | -0.068  | 36.56   |
| ratio_inv_cons      | 1,483     | -0.012   | 0.795   | -1.189  | -0.411  | -0.119           | 0.207   | 16.05   |
| ratio_exp_imp       | 1,483     | -0.004   | 0.945   | -0.055  | -0.055  | -0.006           | -0.055  | 24.98   |
| ratio_fx_cpi        | 1,483     | 0.024    | 1.060   | -0.156  | -0.156  | -0.153           | -0.109  | 20.59   |
| ratio_inv_cons_lag1 | 1,483     | -0.001   | 1.113   | -1.366  | -0.433  | -0.122           | 0.231   | 31.33   |
| ratio_exp_imp_lag1  | 1,483     | 0.001    | 0.999   | -0.055  | -0.055  | -0.007           | -0.055  | 27.09   |
| ratio_fx_cpi_lag1   | 1,483     | 0.013    | 0.908   | -0.139  | -0.139  | -0.137           | -0.100  | 18.46   |


<img width="545" height="391" alt="image" src="https://github.com/user-attachments/assets/6cb36af0-6521-4e91-aa1d-5ea96beedc6b" />

📋 Dataset Comparison Summary

| **Dataset**               | **Rows** | **Crisis Count (1)** | **Non-Crisis Count (0)** | **Crisis %** |
| ------------------------- | -------- | -------------------- | ------------------------ | ------------ |
| Original Training         | 5,929    | 141                  | 5,788                    | 2.38%        |
| Balanced Training (SMOTE) | 11,576   | 5,788                | 5,788                    | 50.00%       |
| Test                      | 1,483    | 35                   | 1,448                    | 2.36%        |




