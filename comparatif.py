import pandas as pd

def estimatePrice(km, theta0, theta1):
    return theta0 + (theta1 * km)

def predict_prices(kms, theta0, theta1):
    predicted_prices = []
    for km in kms:
        predicted_price = estimatePrice(km, theta0, theta1)
        predicted_prices.append(predicted_price)
    return predicted_prices

def training(m, kms, prices):
    learningRate = 0.01
    iterations = 3
    theta0 = 0
    theta1 = 0
    for _ in range(iterations):
        for i in range(m):
            km = kms[i]
            price = prices[i]
            error = estimatePrice(km, theta0, theta1) - price
            tmp0 = learningRate * (1 / m) * error
            tmp1 = tmp0 * km
            theta0 -= tmp0
            theta1 -= tmp1
    return theta0, theta1

if __name__ == "__main__":
    try:
        csv = pd.read_csv("./Subject/data.csv")
        m = len(csv)
        kms = csv['km']
        prices = csv['price']
        theta0, theta1 = training(m - 1, kms, prices)

        # Predict prices for all data points
        predicted_prices = predict_prices(kms, theta0, theta1)

        # Compare predicted prices with actual prices
        for i in range(m):
            print(f"Actual Price: {prices[i]}, Predicted Price: {predicted_prices[i]}")

    except:
        print("Not a good CSV format or can't generate the second predictor program")
