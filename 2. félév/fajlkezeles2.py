import os
import csv
import pandas as pd # terminálba: pip install pandas
import matplotlib.pyplot as plt # pip install matplotlib

PATH_BEMENETEK = os.path.join(os.path.dirname(__file__), "bemenetek")
def opcio1():
    kavezok = []
    with open(os.path.join(PATH_BEMENETEK, "directory.csv"), "r", encoding="utf-8") as f:
        col_names = f.readline().strip().split(",")
        sor = f.readline()
        while sor != "":
            sor = sor.strip().split(",")
            kavezok.append(sor)
            sor = f.readline()
        print(kavezok[:3])

def opcio2():
    kavezok = []
    with open(os.path.join(PATH_BEMENETEK, "directory.csv"), "r", encoding="utf-8") as f:
        data = csv.reader(f, delimiter=",")
        first_row = True
        for row in data:
            if first_row:
                col_names = row
                first_row = False
            else:
                kavezo = {}
                for i in range(len(row)):
                    kavezo[col_names[i]] = row[i]
                kavezok.append(kavezo)
    return kavezok

def opcio3():
    data = pd.read_csv(os.path.join(PATH_BEMENETEK, "directory.csv"))
    return data

data = opcio3()
print(type(data)) # <class 'pandas.core.frame.DataFrame'>
#print(data["Longitude"])
data = data.set_index("Store Number")
print(data)
print(data.loc["22126-218024", "Store Name"]) # Twofour 54
print(data.iloc[3, 1]) # Twofour 54

data = data[["Street Address", "City", "Country", "Postcode", "Longitude", "Latitude"]]
print(data)

magyarok = data[data["Country"] == "HU"] 
print(magyarok)
print(len(magyarok))

orszagonkent = data.groupby("Country").count().reset_index()
orszagonkent = orszagonkent[["Country", "City"]]
orszagonkent.columns = ["Country", "Count"]
orszagonkent = orszagonkent.sort_values(by="Count", ascending = False)
orszagonkent = orszagonkent[orszagonkent["Count"] >= 35]
print(orszagonkent)

plt.bar(orszagonkent["Country"], orszagonkent["Count"])
plt.yscale("log")
plt.xticks(rotation=90)
plt.show()