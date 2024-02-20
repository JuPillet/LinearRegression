# Liste des prix d'origine depuis les données d'entraînement
original_prices = [3650, 3800, 4400, 4450, 5250, 5350, 5800, 5990, 5999, 6200, 6390, 6390, 6600, 6800, 6800, 6900, 6900, 6990, 7490, 7555, 7990, 7990, 7990, 8290]

# Liste des prix estimés depuis les résultats après l'entraînement
estimated_prices = [
    3351.70, 5500.80, 5271.30, 4519.98, 4724.38, 6037.00, 4921.70,
    6590.36, 5399.99, 6697.60, 6739.87, 7146.72, 6912.08, 6408.05,
    7062.21, 6868.65, 7464.69, 6504.57, 7192.00, 7090.65, 7341.04,
    7030.04, 8008.09, 7173.98
]

# Comparaison des prix estimés avec les prix d'origine
for i in range(len(original_prices)):
    original_price = original_prices[i]
    estimated_price = estimated_prices[i]
    difference = original_price - estimated_price
    print(f"Original Price: {original_price:.2f}, Estimated Price: {estimated_price:.2f}, Difference: {difference:.2f}")