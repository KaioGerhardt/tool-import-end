import csv
from functionFiles import *
from functionDB import *

def main():
    
    path = input("Favor, informe o path do arquivo: ")
    path = "table_name.csv"
    table = path.replace(".csv", "")

    dataFile = readFile(path)

    dataSQL = managementSQL(dataFile)
    createTable(dataSQL["header"], "name_table")
    arrInsert = mountInsert(table, dataSQL["header"], dataSQL["data"])

    writeFile("teste2.txt", arrInsert)


main()

