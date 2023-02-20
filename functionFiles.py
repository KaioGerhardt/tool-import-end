import csv
from functionDB import *
import json
from globals import GLOBALS

def readJSON():
    with open('settings.json') as file:
        inputFile = json.load(file) 
    
    return inputFile

# connection data base
GLOBAL = GLOBALS(readJSON())
connection = createServerConnection(GLOBAL["HOST_NAME"], GLOBAL["USER_NAME"], GLOBAL["PASSWORD"], GLOBAL["DB_NAME"])

def readFile(path):
    content  = []
    with open(path, "r") as file:
        fileCSV = csv.reader(file, delimiter=";")

        for num, line in enumerate(fileCSV):
            content.append(line)
    return content

def writeFile(nameArchive, dataLine):
    file = open(nameArchive, "a")

    for dataContent in dataLine:
        file.write(dataContent)
        
    file.close()

def managementSQL(dataFile):
    content = []
    head = ""
    for index, dataFor in enumerate(dataFile):
        if index == 0:
            head = dataFor
        else:
            content.append(dataFor)
    return {
        "header": head,
        "data": content
    }

def mountInsert(table, head, data):
    header = ""
    arr = []
    model = ""
    values = ""

    # mount header
    for indexData, dataHead in enumerate(head) :
        if indexData < (len(head) - 2):
            header += f"{dataHead},"
        else:
            if len(dataHead) > 0:
                header += f"{dataHead}"

    # mount values
    for content in data:
        values = ""
        for dataIndex, dataContent in enumerate(content):
            if dataIndex < (len(content) - 2):
                values += f"'{dataContent.strip()}',"
            else:
                if len(dataContent):
                    values += f"'{dataContent.strip()}'"

        model = f"insert into {table}({header}) values({values});\n"
        arr.append(model)
    
    return arr

def manipulationTable(header):
    cont = 0
    newHeader = []
    for value in header:
        if len(value):
            newHeader.append(value)
            cont += 1
    
    return {
        "newHeader": newHeader,
        "cont": cont
    }

def createTable(header, nameTable):
    head = manipulationTable(header)
    cont = int(len(head["newHeader"]) - 1)

    attributes = ""
    typeAttrivbute = ""

    for index, value in enumerate(head["newHeader"]):
        value = value.replace(" ", "_")
        if index < cont:
            attributes += f"{value} varchar(255),"
        else:
            attributes += f"{value} varchar(255)"
    
    model = f"CREATE TABLE {nameTable}({attributes})"
    executeQuery(connection, model)