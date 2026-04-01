import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

# Load dataset
df = pd.read_csv("cleaned_fitness_data.csv")

# Select features and target variables 
X = df[["steps", "active_minutes", "distance_km"]]           
y = df["calories_burned"]

# Split the data into training and testing sets, 70% train, 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Random Forest 
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Show results
results = X_test.copy()
results["Actual"] = y_test
results["Predicted"] = y_pred
print(results)

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")


# The model performs reasonably well, with a low MAE and MSE, and a high R-squared value. This indicates that the model is able to capture the relationship between the features and the target variable effectively.
# steps, active_minutes, and distance_km all have a very strong relationship with calories burned.


# Save the trained model
import joblib
joblib.dump(model, "calorie_model.pkl")  