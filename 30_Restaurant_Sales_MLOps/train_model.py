import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# 1. Create dummy training data (usually you would load a CSV here)
data = {
    'day_of_week': [1, 2, 3, 4, 5, 6, 7, 1, 2, 3],
    'is_weekend': [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    'promotion': [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    'footfall': [100, 150, 120, 200, 110, 300, 250, 105, 160, 130],
    'sales': [500, 750, 600, 900, 550, 1500, 1200, 520, 800, 650]
}

df = pd.DataFrame(data)

# 2. Define features and target
X = df[['day_of_week', 'is_weekend', 'promotion', 'footfall']]
y = df['sales']

# 3. Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 4. Save the model to a file
joblib.dump(model, 'model.pkl')

print("Model trained and saved successfully as 'model.pkl'.")