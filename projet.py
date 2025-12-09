import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns


print("\n######################################################################")
print("   # PHASE 1 : IMPORTATION  $ AFFICHAGE DE L'ENTETE DU DATA SET      #")
print("######################################################################\n")
fichier = str(input("Entre le nom de ton data set: "))
if not os.path.exists(fichier):
    print("Ce fichier n'a pas ete trouve")
else:
    df = pd.read_csv(fichier)
    print("""
          
AFFICHAGE DE L'ENTETE DE VOS DONNEES """)
print(df.head())

print("\n######################################################################")
print("         #    PHASE 2 : NETTOYAGE DU DATA SET      #")
print("######################################################################\n")
df = df.round(3)
print(f"Nombres de valeurs manquantes par colonnes :\n{df.isna().sum()}")
df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
df['humidity'] = df['humidity'].fillna(df['humidity'].mean())
df['pressure'] = df['pressure'].fillna(df['pressure'].mean())
df["timestamp"] = pd.to_datetime(df["timestamp"])
print(f"Nombres de valeurs manquantes par colonnes apres le nettoyage :\n{df.isna().sum()}")


print("\n######################################################################")
print("    # PHASE 3 :FONCTION POUR L'ANALYSE STATISTIQUE DES  DONNEES     #")
print("######################################################################\n")

def moyenne(colone):
    return sum(colone) / len(colone)
def nbre_ligne(colone):
    return len(colone)
def minimum(colone):
    mini = 1000000000000
    for i in colone:
        if i < mini:
            mini = i
    return mini
def maximum(colone):
    maxi = 0
    for i in colone:
        if i > maxi:
            maxi = i
    return maxi
def modt(colone):
    freq,maxi = {},-1
    for x in colone:
        if x in freq:
            freq[x] +=1
        else :
            freq[x] = 1
    for i in freq:
        if freq[i] > maxi:
            maxi = freq[i]
            x = i
    return (f"{i},{maxi} occurrences")
def mediane(colone):
    colone = sorted(colone)
    n = len(colone)
    if n%2 == 0:
        return colone[n//2]
    else:
        return colone[(n-1)//2]
def variance(colone):
    moy = sum(colone)/len(colone)
    return sum((x-moy)**2 for x in colone)/len(colone)

print(variance(df['temperature']))
print(df.describe())
     
# print("\n######################################################################")
# print("    # PHASE 4 STOCKAGE DES STATISTIQUES DANS UN DICTIONNAIRE     #")
# print("######################################################################\n")

statistiques = {}
for i in ["temperature","humidity","pressure"]:
    statistiques[i] = {
        "moyenne":moyenne(df[i]).__round__(2),
        "minimum":minimum(df[i]),
        "maximum":maximum(df[i]),
        "mode":modt(df[i]),
        "variance":variance(df[i]).__round__(2),
        "mediane":mediane(df[i]).__round__(2)
    }
print("AFFICHAGES DES STATISTIQUES POUR CHAQUE COLONNE: ")
for i,j in statistiques.items():
    print(f"********** affichage des statistiques concernant : {i} **********")
    for cle ,valeur in j.items():
        print(f"{cle}:{valeur}")
    
print("\n######################################################################")
print("    # PHASE 5 VISUALIZATION     #")
print("######################################################################\n")

def figTemperature(): 
    plt.hist(df['temperature'],bins = 20)
    plt.ylabel("Frequence d'apparition")
    plt.xlabel("Temperature en (°C) ")
    plt.title("Proportions des temperatures")
    plt.text("1 -HISTOGRAMMES: l'histogramme montre la repartition des variables , si la distribution est normale et ou se trouve les valeurs frequantes",s="",y="")
    plt.show()
    
    print("""
        2 -COURBE TEMPORELLE montre l'evolution de la temperature dans le temps
        """)
    plt.figure()
    plt.plot(df['timestamp'],df['temperature'])
    plt.xlabel("Timestamp")
    plt.ylabel('Temperature en (°C)')
    plt.title("Courbe temporelle des temperatures")
    plt.show()
    
    print("""
        3 -BOITE A MOUSTACHE: Ici on montre dans une courbe la mediane, les quartiles, les outliers
        """)
    sns.boxplot(x=df['temperature'])
    plt.title("Boite a moustaches de la temperature")
    plt.show()
    
    print("""
        4 -Correlation: RELATION ENTRE TOUTES LES COLONNES
        """)
     
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Heatmap des corrélations")
    plt.show()
    
   
# figTemperature()