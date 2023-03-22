from functions import *

try:

    dict = read_data("winequality.csv")
    dic_red, dic_white = split(dict)
    dict_reduce = reduce(dic_red, "volatile acidity")

except ValueError as err:
    print("Ha ocurrido la excepción" + err)