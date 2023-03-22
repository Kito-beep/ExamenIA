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
                "type": _name,
                "fixed acidity": _adress,
                "volatile acidity": _phone,
                "citric acid": _email,
                "residual sugar": _vip
            }})