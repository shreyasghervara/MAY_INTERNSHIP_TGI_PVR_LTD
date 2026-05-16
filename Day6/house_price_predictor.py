# House Price Predictor using Linear Regression

from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
# House sizes in square feet
house_sizes = np.array([[500], [750], [1000], [1200], [1500], [2000]])

# Corresponding prices in lakhs
house_prices = np.array([25, 38, 50, 60, 75, 100])

# Create and train the model
price_model = LinearRegression()
price_model.fit(house_sizes, house_prices)

# Predict price for a new house
new_house_size = 1100
estimated_price = price_model.predict([[new_house_size]])

# Calculate model performance
accuracy = price_model.score(house_sizes, house_prices)

# Display results
print("===== House Price Prediction =====")
print(f"House Size      : {new_house_size} sqft")
print(f"Estimated Price : ₹{estimated_price[0]:.2f} Lakhs")
print(f"Model Accuracy  : {accuracy:.2%}")