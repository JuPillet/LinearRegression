import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def printRegressionLine(kms, prices, theta0, theta1, ax):
	ax.clear()
	ax.scatter(kms, prices, color='blue', label='Données')
	ax.plot(kms, theta0 + theta1 * kms, color='red', label='linear regression')
	ax.set_xlabel('Kilométrage')
	ax.set_ylabel('Prix')
	ax.legend()
	plt.pause(0.01)

def printModelLR(average, stdDev, theta0, theta1):
	print(f"average: {average}\nstdDev: {stdDev}\ntheta0: {theta0}\ntheta1: {theta1}")
	with open('modelLR', 'w') as ModelLR:
		ModelLR.write(f"average:{average}\n")
		ModelLR.write(f"stdDev:{stdDev}\n")
		ModelLR.write(f"theta0:{theta0}\n")
		ModelLR.write(f"theta1:{theta1}")

def estimatePrice(km, theta0, theta1):
	return theta0 + (theta1 * km)

def averager(m, datas):
	ttlDatas = sum(datas)
	return ttlDatas / m

def diverter(m, datas, average):
	nrmDatas = sum((i - average) ** 2 for i in datas)
	return (nrmDatas / m) ** 0.5

def standardizer(m, datas):
	average = averager(m, datas)
	stdDev = diverter(m, datas, average)
	nrmDatas = [((i - average) / stdDev) for i in datas]
	return average, stdDev, nrmDatas

def training(m, kms, nrmkms, prices, ax):
	learningRate = 0.01
	iterrations = 1000
	midRate = learningRate / m

	theta0 = 0
	theta1 = 0
#boucle principale d'itération d entrainement
	for _ in range (iterrations):
		tmp0 = 0
		tmp1 = 0
#boucle sur chaque valeur de donnée
		for i in range(m):
			km = nrmkms[i]
			price = prices[i]
#calcul d'erreur
			error = estimatePrice(km, theta0, theta1) - price
#calcule temportaire de Theta0 et Theta1
			tmp0 += error
			tmp1 += (error * km)
#ajustement Theta0 et Theta1
		theta0 += midRate * tmp0
		theta1 -= midRate * tmp1
		printRegressionLine(kms, prices, theta0, theta1, ax)
	return theta0, theta1

def	main():
	csv = pd.read_csv("./Subject/data.csv")
	kms = csv['km']
	prices = csv['price']
	m = len(kms)
	average, stdDev, nrmKms = standardizer(m, kms)
	fig, ax = plt.subplots()
	theta0, theta1 = training(m, kms, nrmKms, prices, ax)
	printModelLR(average, stdDev, theta0, theta1)
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
	except Exception as e:
		print(f"Une erreur s'est produite : {e}")