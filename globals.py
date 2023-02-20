def GLOBALS(globals):
    return {
        "HOST_NAME": globals[0]["config"]["hostName"],
        "USER_NAME": globals[0]["config"]["userName"],
        "PASSWORD": globals[0]["config"]["passwd"],
        "DB_NAME": globals[0]["config"]["dbName"],
        "CSV_TO_SQL": globals[1]["resources"]["1"],
        "SQL_TO_CSV": globals[1]["resources"]["2"]
    }