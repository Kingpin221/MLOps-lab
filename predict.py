import joblib

model = joblib.load("billing_model.pkl")

# Example Vodafone customer usage
data_gb = 14
voice_minutes = 550
sms_count = 230
international_minutes = 24

prediction = model.predict([[
    data_gb,
    voice_minutes,
    sms_count,
    international_minutes
]])

print("Vodafone Billing Predictor")
print("--------------------------")
print(f"Data Usage: {data_gb} GB")
print(f"Voice Minutes: {voice_minutes}")
print(f"SMS Count: {sms_count}")
print(f"International Minutes: {international_minutes}")
print(f"Predicted Monthly Bill: £{prediction[0]:.2f}")
