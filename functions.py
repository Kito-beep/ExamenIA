import csv


def read_data(filename):

    dic_datos = {}

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

    valores = []
    for valor in diccionario.items():
        if atributo in valor:
            valores.append(valor[atributo])
    return valores



dict = read_data("winequality.csv")
dic_red, dic_white = split(dict)
dict_reduce = reduce(dic_red, "volatile acidity")

print(dict_reduce)