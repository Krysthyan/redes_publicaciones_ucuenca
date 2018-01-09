import csv

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

option = 2
df = pd.read_excel('datos.xlsx', sheetname='ucuenca')

if option == 1:
    with open('data_co_autores.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for i in df.index:
            print(df['autores'][i].split(","))
            spamwriter.writerow(df['autores'][i].split(",") + [df['revista'][i]])


else:
    with open('data_autores.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for i in df.index:
            print(df['autores'][i].split(","))
            spamwriter.writerow(df['autores'][i].split(","))