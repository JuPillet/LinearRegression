import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def printRegressionLine(ax, kms, pcs, theta0, theta1):
	ax.clear()
	ax.scatter(kms, pcs, color='blue', label='Données')
	ax.plot(kms, theta0 + theta1 * kms, color='red', label='linear regression')
	ax.set_xlabel('Kilométrage')
	ax.set_ylabel('Prix')
	ax.legend()
	plt.pause(0.01)

def printModelLR(theta0, theta1):
	print(f"theta0: {theta0}\ntheta1: {theta1}")
	with open('modelLR', 'w') as ModelLR:
		ModelLR.write(f"theta0:{theta0}\n")
		ModelLR.write(f"theta1:{theta1}")

def estimatePrice(km, theta0, theta1):
	return theta0 + theta1 * km

def diverter(m, datas, average):
	nrmDatas = sum((i - average) ** 2 for i in datas)
	return (nrmDatas / m) ** 0.5

def standardizer(kms, pcs):
	meanKms, meanPcs = np.mean(kms), np.mean(pcs)
	minKm, maxKm, minPc, maxPc = kms.min(), kms.max(), pcs.min(), pcs.max()
	stdKms, stdPcs = (kms - minKm) / (maxKm - minKm), (pcs - minPc) / (maxPc - minPc)
	return meanKms, meanPcs, minKm, maxKm, minPc, maxPc, stdKms, stdPcs
#	stdDev = diverter(m, datas, average)
#	nrmDatas = [((i - average) / stdDev) for i in datas]
#	return average, stdDev, nrmDatas

def training(m, stdKms, stdPcs, minKm, maxKm, minPc, maxPc, ax, kms, pcs):
	learningRate = 0.05
	iterrations = 1000
	midRate = learningRate / m

	theta0 = 0
	theta1 = 0
	deTheta0 = 0
	deTheta1 = 0
#boucle principale d'itération d entrainement
	for _ in range (iterrations):
		tmp0 = 0
		tmp1 = 0
#boucle sur chaque valeur de donnée
		for i in range(m):
			km = stdKms[i]
			price = stdPcs[i]
#calcul d'erreur
			error = estimatePrice(km, theta0, theta1) - price
#calcule temportaire de Theta0 et Theta1
			tmp0 += error
			tmp1 += (error * km)
#ajustement Theta0 et Theta1
		theta0 -= midRate * tmp0
		theta1 -= midRate * tmp1
		deTheta0, deTheta1 = destandardizer(theta0, theta1, minKm, maxKm, minPc, maxPc)
		printRegressionLine(ax, kms, pcs, deTheta0, deTheta1)
	return deTheta0, deTheta1

def destandardizer(theta0, theta1, minKm, maxKm, minPc, maxPc):
	tmpTheta1 = theta1 * (maxPc - minPc) / (maxKm - minKm)
	tmpTheta0 = theta0 * (maxPc - minPc) + minPc - tmpTheta1 * minKm
	return tmpTheta0, tmpTheta1

def	main():
	csv = pd.read_csv("./Subject/data.csv")
	kms = csv['km']
	pcs = csv['price']
	m = len(kms)
	meanKms, meanPcs, minKm, maxKm, minPc, maxPc, stdKms, stdPcs = standardizer(kms, pcs)
	fig, ax = plt.subplots()
	theta0, theta1 = training(m, stdKms, stdPcs, minKm, maxKm, minPc, maxPc, ax, kms, pcs)
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
	except Exception as e:
		print(f"Une erreur s'est produite : {e}")