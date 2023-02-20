from functionFiles import *

def csvToSql(config):
    inputPath = config["inputPath"]
    outputPath = config["outputPath"]
    table = config["nameTable"]

    dataFile = readFile(inputPath)
    dataSQL = managementSQL(dataFile)
    createTable(dataSQL["header"], table)
    arrInsert = mountInsert(table, dataSQL["header"], dataSQL["data"])
    executeInsert(arrInsert)
    writeFileTxt(outputPath, arrInsert)

def sqlToCsv(config):
    queryCSV(config["query"], config["nameFile"], config["header"])