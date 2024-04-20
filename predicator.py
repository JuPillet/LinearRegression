import os
import re
from trainer import estimatePrice

def isKm(entry):
	pattern = r'^[-+]?[0-9]+[.,]?[0-9]?$'
	return bool(re.match(pattern, entry))

def loadModelLR(oldTheta0, oldTheta1):
	path = None
	theta0 = 0
	theta1 = 0
	while (True):
		try:
			print("Veuiller entrer:")
			print("'un/chemin/vers/model/de/donné' pour selectionner celui ci")
			print("'retour' pour concerver le model déjà utilisé")
			print("'exit' pour quitter le programme:")
			print(">>>", end="")
			path = input()
			print("\n----------------------------------------------------------\n")
			if (path == "exit"):
				exit(0)
			elif (path == "retour"):
				return oldTheta0, oldTheta1
			elif (os.path.isfile(path) == False and os.access(path, os.R_OK) == False):
				raise Exception(" 1 : le model est innexistant ou vous ne possedez pas les droits d'accès.")
			with open(path, 'r') as ModelLR:
				lines = ModelLR.readlines()
			if (lines.__len__() != 2):
				raise Exception(
					"2 : format du modelLR invalide\n" +
					"-nombre d'entrée invalid, le format doit etre le suivant:\n\n" +
					"theta0:valeur\n" +
					"theta1:valeur"
				)
			theta0 = lines[0].split(":")
			theta1 = lines[1].split(":")
			if (theta0[0] != "theta0" or theta1[0] != "theta1" or
			theta0.__len__() != 2 or theta1.__len__() != 2):
				raise Exception(
					"3 : format du modelLR invalide\n" +
					"-les 4 entrées doive etre un ensemble 'clef:valeur' comme l'exemple suivant:\n" +
					"theta0:valeur\n" +
					"theta1:valeur"
				)
			try:
				theta0 = float(theta0[1])
				theta1 = float(theta1[1])
				return theta0, theta1
			except Exception as error:
				raise Exception(f"4 : {error}")
		except Exception as error:
			print(f"Error {error}")
			print("\n----------------------------------------------------------\n")

def estimation(km, theta0, theta1):
		estimatedPrice = estimatePrice(km, theta0, theta1)
		if (estimatedPrice < 0):
			estimatedPrice = 0
		print(f"Pour {km:.0f}, le prix est estimé à {estimatedPrice:.2f}")
		print("\n----------------------------------------------------------\n")

if __name__ == "__main__":
	theta0, theta1 = 0, 0
	while (True):
		try:
			print("Veuillez entrez une saisie :")
			print("'model' pour changer de model de donnée")
			print("un kilometrage éguale ou superieur à 0 pour en obenir une estimation")
			print("'exit' pour quitter le programme")
			print(">>>", end="")
			entry = input()
			print("\n----------------------------------------------------------\n")
			if (entry == "model"):
				theta0, theta1 = loadModelLR(theta0, theta1)
			elif (entry == "exit"):
				print("predicator va quitter\n")
				exit(0)
			elif (isKm(entry)):
				km = float(entry)
				if (km < 0):
					raise Exception("5 : le kilometrage ne peut etre négatif")
				estimation(km, theta0, theta1)
			else:
				raise Exception("6 : saissie incorrect")
		except Exception as error:
			print(f"Error {error}")
			print("\n----------------------------------------------------------\n")