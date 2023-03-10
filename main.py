import csv
from functionFiles import *
from functionDB import *
from globals import GLOBALS
from functionsGlobals import *

def main():
    GLOBAL = GLOBALS(readJSON())

    if GLOBAL["CSV_TO_SQL"]["usable"]:
        csvToSql(GLOBAL["CSV_TO_SQL"]["config"])
    elif GLOBAL["SQL_TO_CSV"]["usable"]:
        sqlToCsv(GLOBAL["SQL_TO_CSV"]["config"])

main()

