import pandas as pd
import numpy as np
import sys
#import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def printRegressionLine(ax, kms, pcs, theta0, theta1):
	ax.clear()
	ax.scatter(kms, pcs, color='blue', label='Données')
	ax.plot(kms, theta0 + theta1 * kms, color='red', label='linear regression')
	ax.set_xlabel('Kilométrage')
	ax.set_ylabel('Prix')
	ax.legend()
	plt.pause(0.00001)

def printModelLR(theta0, theta1):
	print(f"theta0: {theta0}")
	print(f"theta1: {theta1}")
	with open('modelLR', 'w') as ModelLR:
		ModelLR.write(f"theta0:{theta0}\n")
		ModelLR.write(f"theta1:{theta1}")

def estimatePrice(km, theta0, theta1):
	return theta0 + theta1 * km

def calculatePrecision(kms, pcs, m, theta0, theta1):
	meanStdPcs = sum(pcs) / m
	estmPcs = estimatePrice(kms, theta0, theta1)
	diffPcs = estmPcs - pcs
#	R²:
##	Sum of Square's Residuals
	ssr = sum((estmPcs - meanStdPcs) ** 2)
##	Sum of Square's total
	sst = sum((pcs - meanStdPcs) ** 2)
##	coefficient of determination
	cod = 1 - ssr/sst
	print(f"coefficient of determination (Precision): {cod}")
#	Root Mean Squared Error
	rmse = np.sqrt(sum(diffPcs ** 2) / m)
	print(f'RMSE : {rmse}')
#	median absolute error
	mae = sum(abs(diffPcs)) / m
	print(f'MAE : {mae}')


#	coefficient of determination

def standardizer(kms, pcs):
	meanKms, meanPcs = np.mean(kms), np.mean(pcs)
	minKm, maxKm, minPc, maxPc = kms.min(), kms.max(), pcs.min(), pcs.max()
	stdKms, stdPcs = (kms - minKm) / (maxKm - minKm), (pcs - minPc) / (maxPc - minPc)
	return meanKms, meanPcs, minKm, maxKm, minPc, maxPc, stdKms, stdPcs
#	stdDev = diverter(m, datas, average)
#	nrmDatas = [((i - average) / stdDev) for i in datas]
#	return average, stdDev, nrmDatas

def destandardizer(theta0, theta1, minKm, maxKm, minPc, maxPc):
	tmpTheta1 = theta1 * (maxPc - minPc) / (maxKm - minKm)
	tmpTheta0 = theta0 * (maxPc - minPc) + minPc - tmpTheta1 * minKm
	return tmpTheta0, tmpTheta1

def training(m, stdKms, stdPcs, minKm, maxKm, minPc, maxPc, ax, kms, pcs):
	learningRate = 0.1
	iterrations = 1000
	midRate = learningRate / m

	stdTheta0 = 0
	stdTheta1 = 0
	theta0 = 0
	theta1 = 0
#boucle principale d'itération d entrainement
	for _ in range (iterrations):
		tmp0 = 0
		tmp1 = 0
#boucle sur chaque valeur de donnée
		for i in range(m):
			km = stdKms[i]
			pc = stdPcs[i]
#calcul d'erreur
			error = estimatePrice(km, stdTheta0, stdTheta1) - pc
#calcule temportaire de Theta0 et Theta1
			tmp0 += error
			tmp1 += (error * km)
#ajustement Theta0 et Theta1
		stdTheta0 -= tmp0 * midRate
		stdTheta1 -= tmp1 * midRate
		theta0, theta1 = destandardizer(stdTheta0, stdTheta1, minKm, maxKm, minPc, maxPc)
		printRegressionLine(ax, kms, pcs, theta0, theta1)
	return theta0, theta1

def test(kms, pcs):
# Données
	km = np.array(kms).reshape(-1, 1)
	price = np.array(pcs).reshape(-1, 1)

# Ajustement du modèle de régression linéaire
	model = LinearRegression()
	model.fit(km, price)

# Prédictions du modèle
	predicted_price = model.predict(km)

# Calcul de SSR
	mean_price = np.mean(price)
	SSR = np.sum((predicted_price - mean_price) ** 2)

# Calcul de SST
	SST = np.sum((price - mean_price) ** 2)

# Calcul de R²
	R_squared = 1 - (SSR / SST)

	print("Coefficient de détermination (R²) :", R_squared)


def	main():
	argc : int | str = len(sys.argv)
	bonus = sys.argv[1] if argc == 2 else False
	if bonus != False and bonus != "bonus":
		raise Exception(f"option '{bonus}' invalide et non reconnu")
	csv = pd.read_csv("./Subject/data.csv")
	kms = csv['km']
	pcs = csv['price']
#	test(kms, pcs)
	m = len(kms)
	meanKms, meanPcs, minKm, maxKm, minPc, maxPc, stdKms, stdPcs = standardizer(kms, pcs)
	fig, ax = plt.subplots()
	theta0, theta1 = training(m, stdKms, stdPcs, minKm, maxKm, minPc, maxPc, ax, kms, pcs)
	cod = calculatePrecision(kms, pcs, m, theta0, theta1)
	printModelLR(theta0, theta1)
	printRegressionLine(ax, kms, pcs, theta0, theta1)
	plt.show()	

if __name__ == "__main__":
	try:
		main()
	except pd.errors.EmptyDataError:
		print("Le fichier CSV est vide.")
	except pd.errors.ParserError:
		print("Format CSV incorrect.")
	except FileNotFoundError:
		print("Le fichier CSV n'a pas été trouvé.")
	#except Exception as e:
	#	print(f"Une erreur s'est produite : {e}")