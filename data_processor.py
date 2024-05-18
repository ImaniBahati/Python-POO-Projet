import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns

class DataAnalysisSystem:

    def __init__(self, data_source):
        self.data_source = data_source
        self.data = pd.read_csv(data_source)

    def clean_data(self):
        # Supprimer les lignes et colonnes vides
        self.data = self.data.dropna()

        # Convertir les types de données
        self.data["nom"] = self.data.astype(str)
        self.data["age"] = self.data.astype(int)
        self.data["sexe"] = self.data.astype(str)
        self.data["salaire"] = self.data.astype(float)
        

        # Remplacer les valeurs manquantes par des valeurs moyennes
        self.data = self.data.fillna(self.data.mean())

    def transform_data(self):
        # Créer des variables catégorielles
        self.data["gender"] = self.data["gender"].astype("category")

        # Créer des variables binaires
        self.data["is_male"] = (self.data["gender"] == "male").astype(int)
        self.data["is_female"] = (self.data["gender"] == "female").astype(int)

        # Créer des variables d'âge
        self.data["age_group"] = pd.cut(self.data["age"], bins=[0, 20, 40, 60, 80], labels=["0-19", "20-39", "40-59", "60-79", "80+"])

    def analyze_data(self):
        # Statistiques descriptives
        print(self.data.describe())

        # Tests t
        print(sklearn.stats.ttest_ind(self.data["income"][self.data["gender"] == "male"], self.data["income"][self.data["gender"] == "female"]))

        # Analyses de corrélation
        print(self.data.corr())

        # Régression linéaire
        model = sklearn.statsmodels.api.OLS(self.data["income"], self.data[["age", "is_male"]])
        results = model.fit()
        print(results.summary())

    def visualize_data(self):
        # Histogramme de l'âge
        plt.hist(self.data["age"])
        plt.xlabel("Age")
        plt.ylabel("Nombre d'individus")
        plt.show()

        # Box plot du revenu par sexe
        sns.boxplot(x="gender", y="income", data=self.data)
        plt.show()

        # Graphique de dispersion de l'âge et du revenu
        plt.scatter(self.data["age"], self.data["income"])
        plt.xlabel("Age")
        plt.ylabel("Revenu")
        plt.show()


if __name__ == "__main__":
    data_analysis_system = DataAnalysisSystem("data.csv")
    data_analysis_system.clean_data()
    data_analysis_system.transform_data()
    data_analysis_system.analyze_data()
    data_analysis_system.visualize_data()