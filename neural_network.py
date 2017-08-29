
import numpy as np
import scipy.linalg as LA
from pandas import DataFrame, ExcelWriter, ExcelFile, read_excel
from random import randint
import csv_utilities as cu

SIZE_OF_DATA = 1017


def main():


    epsilon = 0.0
    terms = 250
    weight_array = [0.5, 0.5, 0.25, 0.25,0.25, 0.25, 0.5, 0.25, 0.25]
    nd_data = cu.read_nparray_from_csv("P_minus2016")
    # print nd_data.shape # np array: (1017,3)
    # pt = nd_data[:,2]
    # print pt.shape # np array: (1017,)

    for i in range(2):
        interate_terms(terms, epsilon, weight_array, nd_data, nd_data[:, 2])
        if epsilon > 0.001:
            epsilon = 0
        else:
            break
    print(weight_array)
    print(epsilon)


def interate_terms(terms, epsilon, listW, listP, listT):
    for i in range(terms):
        rand_index = randint(0, SIZE_OF_DATA - 1)
        p1 = listP[rand_index, 0]
        p2 = listP[rand_index, 1]
        t = listT[rand_index]
        z, y1, y2 = calcZ(p1, p2, listW)
        epsilon = epsilon + pow((z-t),2)
        update_weight(p1, p2, z, t, y1, y2, listW)



def getSheetNames(excelfile):
    return (ExcelFile(excelfile)).sheet_names

def calcZ(x1, x2, listW):
    y1 = (1.0 * listW[0])+(x1 * listW[2])+(x2 * listW[4])
    y2 = (1.0 * listW[1])+(x1 * listW[3])+(x2 * listW[5])
    z = (listW[6] + (np.tanh(y1) * listW[7]) + (np.tanh(y2) * listW[8]))
    return z, y1, y2

def update_weight(x1, x2, z, t, y1, y2, listW):
    listW[0] = listW[0] - (0.001 * (2.0 * (z-t)) * ((1.0 -pow((np.tanh(y1)), 2.0)) * listW[7]))
    listW[1] = listW[1] - (0.001 * (2.0 * (z-t)) * ((1.0 -pow((np.tanh(y2)), 2.0)) * listW[8]))
    listW[2] = listW[2] - (0.001 * (2.0 * (z-t)) * ((1.0 -pow((np.tanh(y1)), 2.0)) * listW[7] * x1))
    listW[3] = listW[3] - (0.001 * (2.0 * (z - t)) * ((1.0 - pow((np.tanh(y2)), 2.0)) * listW[8] * x1))
    listW[4] = listW[4] - (0.001 * (2.0 * (z - t)) * ((1.0 - pow((np.tanh(y1)), 2.0)) * listW[7] * x2))
    listW[5] = listW[5] - (0.001 * (2.0 * (z - t)) * ((1.0 - pow((np.tanh(y2)), 2.0)) * listW[8] * x2))
    listW[6] = listW[6] - (0.001 * (2.0 * (z - t)))
    listW[7] = listW[7] - (0.001 * (2.0 * (z - t)) * np.tanh(y1))
    listW[8] = listW[8] - (0.001 * (2.0 * (z - t)) * np.tanh(y2))

main()