import csv


def read_data(nombre_fichero):

    """
    Esta función recibe el nombre de un fichero csv con muestras de vino,
    y devuelve un diccionario con los datos de las muestras.
    """

    dic_datos = {}
    dato_num = 0

    with open(nombre_fichero, newline='') as csvfile:

        reader = csv.reader(csvfile, delimiter=';')
        next(reader) # Se salta la primera fila con los nombres de las columnas

        for row in reader:

            dato_num += 1
            datos = {}
            pala = {}

            if '' not in row:

                datos['type'] = pala[0]
                datos['fixed acidity'] = float(pala[1])
                datos['volatile acidity'] = float(pala[2])
                datos['citric acid'] = float(pala[3])
                datos['residual sugar'] = float(pala[4])
                datos['chlorides'] = float(pala[5])
                datos['free sulfur dioxide'] = float(pala[6])
                datos['total sulfur dioxide'] = float(pala[7])
                datos['density'] = float(pala[8])
                datos['pH'] = float(pala[9])
                datos['sulphates'] = float(pala[10])
                datos['alcohol'] = float(pala[11])
                datos['quality'] = int(pala[12])

                dic_datos['dato{}'.format(dato_num)] = datos

    return dic_datos

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



dict = read_data("winequality.csv")
print(dict)
