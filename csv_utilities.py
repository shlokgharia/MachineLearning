import csv
import numpy as np
import pandas as pd


def write_data_to_csv_file(file_name, numpy_array):

    fl = open(file_name+'.csv', 'w')
    writer = csv.writer(fl)
    for values in numpy_array:
        writer.writerow(values)
    fl.close()

def read_nparray_from_csv(file_name):
    csv = np.genfromtxt(file_name+'.csv', delimiter=",")
    #print "numpy size: ", csv.shape
    return csv

def exportDfToExcel(filename, column1, colum1_header, column2, colum2_header ):
    outputdf = pd.DataFrame({colum1_header: column1, colum2_header: column2})
    outputdf.to_excel(filename+'.xlsx',sheet_name=filename, index = False)

def getDfFromExcel(filename, sheetname):
    xls_file = pd.ExcelFile(filename+'.xlsx')
    df = xls_file.parse(sheetname)
    return df

def exportDfToCsv(filename, df):
    df.to_csv(filename + ".csv")
