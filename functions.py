import csv
import math


def read_data(filename):

    dic_datos = {}
    dead = 0

    with open(filename, newline='') as csvfile:

        reader = csv.DictReader(csvfile)
        count = 1

        for row in reader:

            if all(row.values()):

                dic_datos.update({"dato"+str(count):
                {
                    "type": row["type"],
                    "fixed acidity": row["fixed acidity"],
                    "volatile acidity": row["volatile acidity"],
                    "citric acid": row["citric acid"],
                    "residual sugar": row["residual sugar"],
                    "chlorides": row["chlorides"],
                    "free sulfur dioxide": row["free sulfur dioxide"],
                    "total sulfur dioxide": row["total sulfur dioxide"],
                    "density": row["density"],
                    "pH": row["pH"],
                    "sulphates": row["sulphates"],
                    "alcohol": row["alcohol"],
                    "quality": row["quality"]
                },})

                count += 1
            else: 
                dead += 1

        if dead >= 50:
            raise ValueError("Maracatón")
        
    return dic_datos

def split(dic_muestras):

    dic_red = {i:dic_muestras[i] for i in dic_muestras if dic_muestras[i]['type'] == "red"}
    dic_white = {i:dic_muestras[i] for i in dic_muestras if dic_muestras[i]['type'] == "white"}

    return [dic_red, dic_white]

def reduce(diccionario, atributo):

    """
    Esta función recibe un diccionario y el nombre de un atributo,
    y devuelve una lista con los valores de dicho atributo en el diccionario.
    """
    keys = diccionario.keys()

    valores = []
    for valor in diccionario.items():
        if atributo in valor:
           valores.append(valor[atributo])
    return valores


def silhouette(lista):

    coeficientes = []

    for i in range(len(lista)):

        # Distancia media a(i) entre i y el resto de valores de la lista
        a_i = sum([math.sqrt(sum([(lista[i][j]-lista[k][j])**2 for j in range(len(lista[i]))])) for k in range(len(lista)) if k != i]) / (len(lista)-1) # ufff...

        # Agrupar los elementos de la lista en función de su clase
        grupos = {}

        for k in range(len(lista)):
            if k != i:
                clase = lista[k][-1]
                if clase not in grupos:
                    grupos[clase] = []
                grupos[clase].append(lista[k])

        # Distancia media b(i) entre i y todos los elementos de la lista que no están en la misma clase que i
        b_i = min([sum([math.sqrt(sum([(lista[i][j]-x[j])**2 for j in range(len(lista[i])-1)])) for x in grupos[clase]])/len(grupos[clase]) for clase in grupos]) # madre...

        # Coeficiente S(i)
        s_i = (b_i - a_i) / max(a_i, b_i)
        coeficientes.append(s_i)

    # Coeficiente de Silhouette de la lista
    silhoutte_coef = sum(coeficientes) / len(coeficientes)

    return silhoutte_coef


dict = read_data("winequality.csv")
dic_red, dic_white = split(dict)
dict_reduce = reduce(dic_red, "volatile acidity")
res = silhouette([1, 5, 8, 2])

print(res)

