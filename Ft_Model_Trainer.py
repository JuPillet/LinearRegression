import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tools import  extractDatas 
from tools import visualizeDataSet


class Ft_Linear_Regression() :

    def __init__(self, datas) :

        self.originalDataSet = datas

        # [ Melange le DataSet pour assurer meilleure neutralite du model ]
        self.dataSet = self.originalDataSet.sample(frac=1).reset_index(drop=True)
        self.xName = self.dataSet.columns[0]
        self.yName = self.dataSet.columns[1]
        self.xColumn =self.dataSet[self.xName]
        self.yColumn =self.dataSet[self.yName]
        self.n = len(self.xColumn)

        # [ Imput Values to train the Model ]
        self.iteration = 0
        # self.while_turns = 0
        self.learning_rate = 0.01
        self.max_iterations = 10000
        self.convergence_threshold = 0.001
        self.theta_0 = 0
        self.theta_1 = 0
        self.tmp_theta_0 = 0
        self.tmp_theta_1 = 0
        
        self.cost = 0
        self.tmp_cost = 0
        self.cost_evolution = []

        # [ Metrics for Standardization ] (Normalisation des donnees)
        # -> Std by min and max (Atenuation des extremes)
        self.xMin = 0
        self.xMax = 0
        self.yMin = 0
        self.yMax = 0
        self.xMean = 0
        self.yMean = 0

        # [ Columns X and Y Standardized ]
        self.X = 0
        self.Y = 0
        self.rev_theta_0 = 0
        self.rev_theta_1 = 0
        self.standardizeDataSet()
        self.correlation_coefficient = self.getCorrelationCoefficient()


        # [ Launch Model ]
        self.model()
        self.plot_cost_function()
        self.reverse_normalisation()
        self.plot_values_and_results(False)
        self.plot_values_and_results(True)
        self.evaluateModel()


# - # - # - #  - # - # - [  Functions  ] - # - # - # - #  - # - # - #  
    def cost_function(self, X, y, theta_0, theta_1):
        predictions = theta_0 + theta_1 * X
        cost = (1 / (2 * self.n)) * np.sum((predictions - y)**2)
        return cost


    def model(self) :
        print('\n # # # # # [ Train Model ] # # # # # # # # #')
        self.iteration = 0
        while True :
            current_cost = 0
            # Calcul de la derivee partielle par rapport a theta_0
            self.tmp_theta_0 = (1 / self.n) * np.sum(self.theta_0 + self.theta_1 * self.X - self.Y)
            # Calcul de la derivee partielle par rapport a theta_1
            self.tmp_theta_1 = (1 / self.n) * np.sum((self.theta_0 + self.theta_1 * self.X - self.Y) * self.X)

            # MaJ param
            self.theta_0 = self.theta_0 - self.learning_rate * self.tmp_theta_0
            self.theta_1 = self.theta_1 - self.learning_rate * self.tmp_theta_1

            # Calcul fct de cout
            self.cost = self.cost_function(self.X, self.Y, self.theta_0, self.theta_1)
            self.cost_evolution.append(self.cost)

            # Verif evolution convergence
            if self.cost < self.convergence_threshold :
                break

            # Verif nbr i
            self.iteration += 1
            if self.iteration >= self.max_iterations :
                break

            #Print cost evolution
            if self.iteration % (self.max_iterations / 10) == 0 :
                print(f'i[{self.iteration}] \tcost: [ {self.cost} ]')

        print(f'i[{self.iteration}]   last cost: [ {self.cost} ]')
        print(f' theta_0: [ {self.theta_0} ] (standardized)\n theta_1: [ {self.theta_1} ] (standardized)')
        self.plot_Standardized_results()
        print(' # # # # # # # # # # # # # # # # # # # # # #\n')


    def getCorrelationCoefficient(self) :
        # Somme des Ecarts a la Moyenne de 'x' * Ecart a la moyenne de 'y'
        numerator = np.sum((self.xColumn - self.xMean) * (self.yColumn - self.yMean))
        # Racine de la Somme des Ecarts a la Moyenne de 'x' au Carre * Somme Ecart a la moyenne de 'y' au Carre
        denominator = np.sqrt(np.sum((self.xColumn - self.xMean)**2) * np.sum((self.yColumn - self.yMean)**2))
        correlation_coefficient = numerator / denominator
        print(f'Coef Correlation du DataSet: \t[ {correlation_coefficient:.2f} ]')
        return correlation_coefficient

    def evaluateModel(self) :
        print('\n # # # # # [ Model Evaluation ] # # # # # # #')
        predictions = self.rev_theta_0 + (self.rev_theta_1 * self.xColumn)
        sommeEcartsCarre = np.sum((self.yColumn - self.yMean)**2)
        sommeCarreResiduels = np.sum((self.yColumn - predictions)**2)
        coefDetermmination = 1 - ( sommeCarreResiduels / sommeEcartsCarre )
        rCarre = coefDetermmination * 100
        print(f'Fiabilite du Modele: \t[ {rCarre:.2f} % ]\n   ->  Coefficient de determination')
        print(f'   ->  {rCarre:.2f} % de la Variance totale des donnees peut ainsi etre expliquee par le Modele')

        ecartsCarre = ( (self.yColumn - predictions)**2 )
        moyenneCarreEcarts = np.mean(ecartsCarre)
        racineCarreEcarts = np.sqrt(moyenneCarreEcarts)
        print(f'Precision du Modele: \t[ $ {racineCarreEcarts:.2f} ]\n   ->  Erreur Quadratique Moyenne')
        print(f"   ->  Calcul de la mesure de l'ecart moyen de precision du modele qui est a Plus ou Moins $ {racineCarreEcarts}\n")


# - # - # - # - # [ Normalisation des Datas ] # - # - # - # - #
    def standardizeDataSet(self) :
        print(' # # # # # [ Standardization ] # # # # # #')
        # [ Moyenne Columns X et Y ]
        self.xMean = np.mean(self.xColumn)
        self.yMean = np.mean(self.yColumn)
        print(f'xMean : [ {self.xMean:.2f} ]  \tyMean : [ {self.yMean:.2f} ]')

        # [ Min et Max Columns X et Y ]
        self.xMin = self.xColumn.min()
        self.xMax = self.xColumn.max()
        self.yMin = self.yColumn.min()
        self.yMax = self.yColumn.max()
        print(f'xMax  : [ {self.xMax} ]  \tyMax :  [ {self.yMax} ]')
        print(f'xMin  : [ {self.xMin} ]  \tyMin  : [ {self.yMin} ]')

        # [ Normalisation xColumn en 'X' et yColumn en 'Y']
        self.stanardizationByMinMax()
        self.displayStandardizedDatas('MinMax')
        print(' # # # # # # # # # # # # # # # # # # # # # #\n')


    def stanardizationByMinMax(self) :
        print('Standardize  By  Min  &  Max...')
        try :
            X = self.dataSet.iloc[:, 0].values
            Y = self.dataSet.iloc[:, 1].values
            self.X = (self.xColumn - self.xMin) / ( self.xMax - self.xMin)
            self.Y = (self.yColumn - self.yMin) / ( self.yMax - self.yMin)
            # print(f' * [ X ] *: {self.X},\n * [ Y ] *: {self.Y}')

        except ValueError:
            print( ' [ >< F a i l >< ]-  ->: \t', ValueError)


    def reverse_normalisation(self) :
        print('\n # # # # # [ Final Results ] # # # # # # # # #')
        self.rev_theta_1 = (self.yMax - self.yMin) * self.theta_1 / (self.xMax - self.xMin)
        self.rev_theta_0 = self.yMin + ((self.yMax - self.yMin) * self.theta_0) + self.rev_theta_1 * (1 - self.xMin) 
        print(f'Final Thetas :\n  -> theta_0 : [ {self.rev_theta_0} ]\n  -> theta_1 : [ {self.rev_theta_1} ]')


# - # - # - #  - # - # - [  Display Datas  ] - # - # - # - #  - # - # - #  
    def displayStandardizedDatas(self, methodName) :
        plt.title(f" Standardized Datas by [ {methodName} ]'s method")
        plt.xlabel(f'{self.xName} Standardized')
        plt.ylabel(f'{self.yName} Standardized')
        plt.scatter(self.X, self.Y)
        plt.show()

    def plot_Standardized_results(self) :
        plt.title(f' Resultat (stdzed) pour [ {self.iteration} ] iter avec un \'pas\' de ( {self.learning_rate} )')
        plt.xlabel(self.xName)
        plt.ylabel(self.yName)
        plt.scatter(self.X, self.Y)
        Xmean = np.sum(self.X / self.n)
        Ymean = np.sum(self.Y / self.n)
        plt.scatter(Xmean, Ymean, c='y')
        plt.plot(self.X, self.theta_1 * self.X + self.theta_0, c='r')
        plt.show()

    def	plot_cost_function(self) :
        plt.title(f' Cost Function pour [ {self.iteration} ] iterations ')
        plt.xlabel("nombre d'iteration / epoch")
        plt.ylabel('ecarts - couts')
        plt.plot(range(self.iteration), self.cost_evolution)
        plt.show()

    def plot_values_and_results(self, print) :
        plt.xlabel(self.xName)
        plt.ylabel(self.yName)
        plt.scatter(self.xColumn, self.yColumn)
        plt.scatter(self.xMean, self.yMean, c='y')
        plt.plot(self.xColumn, self.rev_theta_1 * self.xColumn + self.rev_theta_0, c='r')

        if (print == True) :
            # Resolution par la methode des moindres carres 
            plt.title(f' Resultat [ {self.iteration} ] iterations \'pas\' de ( {self.learning_rate} ) \net Droite Optimale (vert) par la Methode des Moindres Carres')
            x = self.xColumn
            y = self.yColumn
            n = self.n
            a = (n * (x*y).sum() - x.sum()*y.sum()) / (n*(x**2).sum() - (x.sum())**2)
            b = ((x**2).sum()*y.sum() - x.sum() * (x*y).sum()) / (n * (x**2).sum() - (x.sum())**2)
            plt.plot(self.xColumn, a * self.xColumn + b, c='g')
        else :
            plt.title(f' Resultat pour [ {self.iteration} ] iterations avec un \'pas\' de ( {self.learning_rate} ) - lr')

        plt.show()




def main() :
    if len(sys.argv) != 2 :
        csv_file_path = './data.csv'
    else :
        csv_file_path = sys.argv[1]
    try :    
        dataSet = extractDatas(csv_file_path)
        visualizeDataSet(dataSet)
        lrModel = Ft_Linear_Regression(dataSet)
    except ValueError :
        return

if __name__ == "__main__" :
    main()