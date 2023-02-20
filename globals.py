def GLOBALS(globals):
    return {
        "HOST_NAME": globals[0]["config"]["hostName"],
        "USER_NAME": globals[0]["config"]["userName"],
        "PASSWORD": globals[0]["config"]["passwd"],
        "DB_NAME": globals[0]["config"]["dbName"],
    }