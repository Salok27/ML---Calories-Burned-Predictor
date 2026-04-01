
#  Calories Burned Predictor

##  Project Overview

The **Calories Burned Predictor** is an end-to-end machine learning project that estimates calories burned based on daily physical activity. From **data exploration** to a fully **interactive web application**, this project demonstrates a complete data science workflow.

###  App Demo

Interactively predict calories burned with our Streamlit dashboard:

![Screenshot_1-4-2026_15271_localhost](https://github.com/user-attachments/assets/be7fcb31-b845-4d75-9007-551e25d15eb1)
![Screenshot_1-4-2026_15271_localhost](https://github.com/user-attachments/assets/be7fcb31-b845-4d75-9007-551e25d15eb1)
*Example of the deployed app where users can input activity data.*

---

##  Data Analysis

The analysis began with the `steps_tracker_dataset.csv` dataset to understand patterns and relationships in user activity:

* Strong correlations were observed between:

  * `distance_km`
  * `calories_burned`
  * `steps`
  * `active_minutes`
* Visualizations included:

  * Scatter plots
  * Correlation heatmaps

###  Correlation Heatmap

![Correlation Heatmap Screenshot](screenshots/heatmap.png)
*Shows relationships between features and calories burned.*

###  Scatter Plots

![Scatter Plot Screenshot](screenshots/steps_vs_calories.png)
*Steps vs. Calories Burned to visualize the linear relationship.*

---

##  Data Preparation

To optimize model performance, the dataset was refined:

* Exported a cleaned dataset: `cleaned_fitness_data.csv` containing **only the four most relevant features**
* Removed irrelevant columns such as `date` and `mood`
* Handled missing values and ensured data consistency

This preprocessing ensures the model focuses on the strongest predictors of calorie expenditure.

---

##  Machine Learning Model

The predictive model leverages **Random Forest Regression** to accurately estimate energy expenditure:

* Dataset split: **70% training**, **30% testing**
* Trained a `RandomForestRegressor` to capture non-linear relationships
* Model performance validated on the test set
* Final model saved as `calorie_model.pkl` for deployment

###  Model Performance

![Prediction vs Actual Screenshot](screenshots/prediction_vs_actual.png)
*Comparison of predicted vs. actual calories burned.*

###  Feature Importance

![Feature Importance Screenshot](screenshots/feature_importance.png)
*Highlights the most influential variables in the model.*

---

##  Automation

A streamlined workflow allows full pipeline execution with minimal effort:

* `run.bat` automates:

  1. Model training (`ml_model.py`)
  2. Launching the interactive web app (`app.py`)
* Simplifies end-to-end testing and deployment

---

##  Setup and Usage

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Full Pipeline

```bash
.\run.bat
```

### 3. Or Launch the Dashboard Directly

```bash
streamlit run app.py
```

---
