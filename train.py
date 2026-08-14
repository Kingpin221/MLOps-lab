import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load Vodafone billing data
data = pd.read_csv("data/billing.csv")

# Features
X = data[
    [
        "data_gb",
        "voice_minutes",
        "sms_count",
        "international_minutes"
    ]
]

# Target
y = data["bill_amount"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

print("Vodafone Billing Model")
print("----------------------")
print(f"Mean Absolute Error: {mae:.2f}")

# Quality gate
if mae > 10:
    print("MODEL FAILED QUALITY GATE")
    print("MAE must be <= 10")
    raise SystemExit(1)

# Save model
joblib.dump(model, "billing_model.pkl")

print("MODEL PASSED QUALITY GATE")
print("Model saved as billing_model.pkl")
