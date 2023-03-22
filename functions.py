import csv

def read_data(nombre_fichero):

    dic_datos = {}

    with open(nombre_fichero, 'r') as muestras:
        c = 0
        reader = csv.reader(muestras)
        for row in reader:
            c = c+1

            dic_datos.update({"dato"+c:
            {
                "type": ,
                "fixed acidity": _adress,
                "volatile acidity": _phone,
                "citric acid": _email,
                "residual sugar": _vip
                "chlorides":
                "free sulfur dioxide":
                "total sulfur dioxide":
                "density":
                "pH":
                "sulphates":
                "alcohol":
                "quality":
            },})


def split(dic_muestras):

    dic_red = {i:dic_muestras[i] for i in dic_muestras if dic_muestras[i]['type'] == "red"}
    dic_white = {i:dic_muestras[i] for i in dic_muestras if dic_muestras[i]['type'] == "white"}

    return [dic_red.pop, dic_white]


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